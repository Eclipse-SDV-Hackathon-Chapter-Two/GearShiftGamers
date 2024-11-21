# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install build tools and other dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-rpi.gpio

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
# COPY adapters/joystick_adapter.py /app
COPY adapters /app/adapters

# Install Python dependencies
RUN pip install --no-cache-dir pygame kuksa_client adafruit-blinka adafruit-platformdetect RPi.GPIO adafruit-circuitpython-ads1x15

# Command to run your application
CMD ["python", "adapters/joystick_adapter.py"]
