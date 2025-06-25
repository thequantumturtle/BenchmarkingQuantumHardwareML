<<<<<<< lj1txa-codex/create-benchmarking-framework-for-quantum-hardware
FROM python:3.10-slim

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

# Copy source code
WORKDIR /app
COPY . /app

# Default command runs the basic benchmark. Override to run others.
=======
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
>>>>>>> main
CMD ["python", "-m", "benchmarking.benchmark"]
