FROM python:2.7
ENV PYTHONUNBUFFERED 1

ENV APP_ROOT /app

WORKDIR /app

RUN  apt-get update && apt-get install -y mysql-client && apt-get clean

COPY ./config/requirements.txt /app/config/requirements.txt
COPY ./config/sql/1-modified_django.sql /app/config/sql/1-modified_django.sql
RUN pip install -r /app/config/requirements.txt
COPY . /app


