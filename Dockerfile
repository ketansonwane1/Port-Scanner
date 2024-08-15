FROM python:3.8-slim

# Create a non-root user and switch to it
RUN useradd -m myuser
USER myuser

# Set the working directory
WORKDIR /app

# Copy the application code and requirements
COPY --chown=myuser:myuser index.py /app
COPY --chown=myuser:myuser requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "index.py"]
