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

# openai>=3 uses httpx2, which verifies TLS against the OS trust store by default.
# Debian's ca-certificates lacks "emSign ECC Root CA - G3" (root of the InCommon
# chain served by api.delphi.jlab.org), so point it at certifi's newer bundle.
ENV SSL_CERT_FILE=/app/.venv/lib/python3.13/site-packages/certifi/cacert.pem

# Copy application source
COPY main.py kg_agent.py ./

EXPOSE 7860

# Run with uv so the virtualenv is activated automatically
CMD ["uv", "run", "python", "main.py"]
