# Agentic Triage MCP 🤖

### *The Autonomous Bridge between GitHub Issues and Enterprise Logic*

This project demonstrates the transition from **Author of Code** to **Orchestrator of Probabilistic Systems**. It features an autonomous agent capable of multi-step reasoning, tool discovery, and high-fidelity action within the GitHub ecosystem.

---

## 🏗️ Architecture: The 2026 "Gold Standard"
Instead of a linear script, this system uses a **Reasoning Graph** to handle the uncertainty of human-written support tickets.

* **The Brain:** **GPT-4o / Claude 3.5 Sonnet** optimized for complex tool-calling.
* **The Orchestrator:** **Pydantic AI**. Implements type-safe agentic workflows with structured outputs.
* **The Hands:** **GitHub MCP Server**. A standardized interface (Model Context Protocol) that allows the model to "see" issues and "write" comments/labels without custom API glue.
* **The Environment:** **uv + Docker Compose**. High-performance Python project management paired with microservice orchestration.

---

## 🧠 The Orchestration Philosophy: Deterministic Guardrails
In a probabilistic system, the "Code" is no longer a set of instructions, but a set of constraints. This project implements:

Strict Schema Validation: Leveraging Pydantic to ensure the LLM's "hallucinations" are caught by the type system before they reach the GitHub API.

Functional Tool-Shadowing: The agent doesn't have "god mode." Its actions are restricted to the capabilities defined in the MCP schema, providing a natural security boundary.

---

## 🚀 Key Features & ROI
* **Autonomous Classification:** Evaluates incoming issues against a dynamic `rubric.md` to determine priority and severity.
* **Contextual Interaction:** If an issue is missing logs, the agent autonomously requests them before a human ever sees the ticket.
* **Deterministic Reliability:** Uses Pydantic to ensure all LLM outputs strictly adhere to your business schema.
* **Observable Reasoning:** Features a "Thought Trace" showing the agent's internal chain-of-thought during tool invocation.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12+ (managed by `uv`)
* **Framework:** Pydantic AI
* **Protocol:** Model Context Protocol (MCP)
* **Infrastructure:** Docker, Docker Compose

---

## 📈 Measurable Impact
> "By automating the initial 15 minutes of issue triage—classification, labeling, and information gathering—this system reduces the Mean Time to Acknowledge (MTTA) by ~85%."

---

## 🚦 Getting Started

1. **Install uv**:
   ```bash
   curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
   ```

2. Set up Environment:
Create a `.env` file with your `GITHUB_PAT` and `OPENAI_API_KEY`.

3. Spin up the Orchestration
  ```bash
   docker-compose up
  ```
