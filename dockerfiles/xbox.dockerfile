# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY adapters/xbox_adapter.py /app

# Install Python dependencies
RUN pip install --no-cache-dir pygame kuksa_client

# Command to run your application
CMD ["python", "xbox_adapter.py"]
