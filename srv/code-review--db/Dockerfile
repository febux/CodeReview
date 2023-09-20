FROM python:3.10-slim

WORKDIR /docker_app

COPY ./src /docker_app/src
COPY pyproject.toml /docker_app/pyproject.toml

RUN python -m pip install --upgrade pip && python -m pip install --upgrade build
RUN --mount=type=cache,target=/root/.cache/pip \
      python -m pip install .

WORKDIR /docker_app/src/code_review__web
