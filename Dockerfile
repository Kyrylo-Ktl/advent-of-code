FROM python:3.12-slim

WORKDIR /app

# Copy infrastructure for solutions
COPY infrastructure ./infrastructure

# Install infrastructure dependecies
RUN pip install --upgrade pip && \
    pip install --upgrade --no-cache-dir -r infrastructure/requirements.txt

# Copy input for solutions
COPY inputs ./inputs

# Copy solutions code
COPY solutions ./solutions

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
