# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables to make Python output work without buffering, and ensure that no .pyc files are written
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR ./app

# Copy the current directory contents into the container at /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt


# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]