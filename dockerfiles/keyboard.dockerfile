# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY adapters/keyboard_adapter.py /app
COPY adapters/parameters.py /app

# Install Python dependencies
RUN pip install --no-cache-dir kuksa-client
RUN apt-get update && apt-get install -y --no-install-recommends xdotool && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Command to run your application
CMD ["python", "keyboard_adapter.py"]
