FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
	&& apt-get install -y --no-install-recommends git ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/Mandoa-Labs/Scarif.git --depth 1 /tmp/scarif \
	&& cp -a /tmp/scarif/data ./data \
	&& rm -rf /tmp/scarif

# Copy application source
COPY mcp_server.py search.py ./

# MCP servers communicate over stdio
ENTRYPOINT ["python", "mcp_server.py"]
