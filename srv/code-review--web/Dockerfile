FROM python:3.10

WORKDIR /docker_app

COPY ./src /docker_app/src
COPY pyproject.toml /docker_app/pyproject.toml
COPY README.md /docker_app/README.md

RUN python -m pip install --upgrade pip && python -m pip install --upgrade build
RUN --mount=type=cache,target=/root/.cache/pip \
      python -m pip install .

WORKDIR /docker_app/src/code_review__web
RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["sh", "entrypoint.sh"]