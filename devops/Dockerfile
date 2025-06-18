# Use the official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Install Python dependencies early to cache better
COPY /requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app code into the container
COPY backend/ backend/
