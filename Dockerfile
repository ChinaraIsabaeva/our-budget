# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /webapp/src
RUN apt-get update && apt-get -y install \
    libpq-dev \
    gcc \
    postgresql-client
RUN pip install --upgrade pip
COPY requirements /webapp/src/requirements/
RUN pip install --user -r requirements/dev.txt -r requirements/ci.txt
COPY . /webapp/src
