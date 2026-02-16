services:
  # The "Hands": Official GitHub MCP Server
  mcp-github:
    image: ghcr.io/github/github-mcp-server:latest
    environment:
      - GITHUB_PERSONAL_ACCESS_TOKEN=${GITHUB_PAT}
      # Restrict tools to only what the triage bot needs
      - GITHUB_TOOLSETS=issues,repos,pull_requests
    ports:
      - "8080:8080"
    restart: always

  # The "Brain": Your Pydantic AI Bot
  triage-bot:
    build: .
    depends_on:
      - mcp-github
    environment:
      - GITHUB_MCP_URL=http://mcp-github:8080/sse  # Network-based transport
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./src:/app/src
      - ./data:/app/data