FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY . .
RUN ls


EXPOSE 8000
