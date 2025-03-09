# Use a lightweight Python image
FROM python:3.10-slim

# Set environment variables to avoid buffering issues
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the correct port for health checks
EXPOSE 8000

# Run Flask with Gunicorn on port 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
