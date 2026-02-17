FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY . .
# This ensures uvicorn keeps the container alive indefinitely
CMD ["uv", "run", "uvicorn", "src.agent:app", "--host", "0.0.0.0", "--port", "8000"]