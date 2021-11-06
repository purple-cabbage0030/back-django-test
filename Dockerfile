# pull official base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECRET_KEY

ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY

# set work directory
RUN mkdir /backend
WORKDIR /backend

COPY . /backend/
EXPOSE 8000
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python manage.py makemigrations
# RUN python manage.py migrate