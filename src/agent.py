import os
from fastapi import FastAPI, Request
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerSSE
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# 1. SETUP THE HANDS (The connection to the GitHub tools)
github_server = MCPServerSSE(url=os.getenv("GITHUB_MCP_URL", "http://mcp-github:8080/sse"))

# 2. SETUP THE BRAIN (The logic and rubric)
triage_agent = Agent(
    'openai:gpt-4o',
    toolsets=[github_server],
    system_prompt=(
        "You are an autonomous GitHub Support Triage Bot. "
        "When an issue is opened, analyze it and apply priority labels (P0, P1, P2) "
        "based on the critical nature of the report."
    )
)

@app.post("/webhook")
async def github_webhook(request: Request):
    data = await request.json()

    # Log the incoming event for debugging
    print(f"received event: {data.get('action')}")

    if data.get("action") == "opened":
        issue_body = data["issue"]["body"]
        issue_url = data["issue"]["html_url"]

        print(f"🚀 New Issue detected! URL: {issue_url}")

        # The actual triage happens here
        await triage_agent.run(
            f"Triage this specific issue: {issue_url}. "
            f"Content: {issue_body}. "
            "Analyze and apply the correct label now."
        )

    return {"status": "accepted"}

# Added a health check so you can verify the bot is alive in your browser
@app.get("/health")
async def health():
    return {"status": "online"}