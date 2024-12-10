# Use the official Python slim image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies and clean up to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Default command to run the Django application
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
