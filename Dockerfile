# Dockerfile
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application code and requirements
COPY index.html /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "index.html"]
