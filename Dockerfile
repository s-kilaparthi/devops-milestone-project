# Base image - official Python 3.11 slim version
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY app/ ./app/
COPY scripts/ ./scripts/

# Set environment variables
ENV APP_ENV=production
ENV APP_PORT=8080

# Default command when container starts
CMD ["python3", "app/main.py"]
