# syntax=docker/dockerfile:1
FROM python:latest
RUN python -m pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN python -m pip install -r /code/requirements.txt
