# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/data /app/output /app/logs

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV DATA_PATH=/app/data/train.csv

# Command to run the pipeline
CMD ["python", "main.py"]