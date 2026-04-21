FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY mcp_server.py search.py ./
COPY data/ data/

# MCP servers communicate over stdio
ENTRYPOINT ["python", "mcp_server.py"]
