# syntax=docker/dockerfile:1

FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Set working directory
WORKDIR /app

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock .python-version ./

# Install dependencies (frozen from lockfile, no dev deps)
RUN uv sync --frozen --no-dev --no-install-project

# Copy application source
COPY main.py kg_agent.py ./

EXPOSE 7860

# Run with uv so the virtualenv is activated automatically
CMD ["uv", "run", "python", "main.py"]
