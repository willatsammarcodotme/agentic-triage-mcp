# Agentic GitHub Triage Bot

Real-time issue triage using the Model Context Protocol (MCP) to decouple the GitHub toolset from the core agent logic. The bot's "hands" are interchangeable and the whole thing runs locally against real GitHub webhook events.

## How it works

The GitHub MCP Server runs behind `mcp-proxy` to expose GitHub's toolset over SSE. Pydantic AI handles the agent logic and keeps LLM outputs type-safe. ngrok runs as a sidecar to forward real GitHub webhook events during development.

When an issue comes in, the agent evaluates it against a `rubric.md`, applies labels and priority, and requests missing information (like logs) before a human ever sees the ticket.

## Stack

- **Pydantic AI** — type-safe agent logic and structured LLM outputs
- **GitHub MCP Server** — standardized GitHub tooling over MCP
- **mcp-proxy** — SSE transport layer for the MCP server
- **Docker Compose** — single-command orchestration

## Getting Started

Create a `.env` file with your credentials:
```env
GITHUB_PAT=your_github_pat
OPENAI_API_KEY=your_openai_api_key
NGROK_TOKEN=your_ngrok_token
```

Then:
```bash
docker compose up --build
```