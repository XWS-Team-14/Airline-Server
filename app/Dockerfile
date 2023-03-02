# syntax=docker/dockerfile:1
FROM --platform=$BUILDPLATFORM python:3.9-bullseye AS builder
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
CMD ["manage.py", "runserver", "0.0.0.0:8000"]


