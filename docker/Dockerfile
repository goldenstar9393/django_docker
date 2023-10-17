# Use an official Python runtime as a parent image
FROM python:3.9.6

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE techtest.settings

# Create and set the working directory
RUN mkdir /django-tech-test
WORKDIR /django-tech-test

# Copy the requirements file into the container
COPY requirements.txt /django-tech-test/docker/

# Install the project's dependencies
RUN pip install -r docker/requirements.txt

# Copy the Django project code into the container
COPY . /django-tech-test/
