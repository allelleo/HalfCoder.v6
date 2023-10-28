# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in docker
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]