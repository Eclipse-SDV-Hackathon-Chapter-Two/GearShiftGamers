# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY adapters/joystick_adapter.py /app

# Install Python dependencies
RUN pip install --no-cache-dir pygame kuksa_client adafruit-blinka adafruit-platformdetect 

# Command to run your application
CMD ["python", "joystick_adapter.py"]
