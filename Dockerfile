FROM python:3.10-slim

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

# Copy source code
WORKDIR /app
COPY . /app

# Default command runs the basic benchmark. Override to run others.
CMD ["python", "-m", "benchmarking.benchmark"]
