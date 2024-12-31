# Use the official Python image as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN python -m pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "run.py"]
