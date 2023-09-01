# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /docker_app

# copy project
COPY ./src /docker_app/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY setup.py /docker_app/setup.py
RUN python setup.py install

RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache \
    pip install -r src/code_review__web/requirements.txt

RUN export PATH=/usr/lib/postgresql/14.8/bin/:$PATH

WORKDIR /docker_app/src/code_review__web
