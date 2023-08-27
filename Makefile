SHELL := /bin/bash
CWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ME := $(shell whoami)

nothing:
	@echo "do nothing"

fix_permissions:
	@echo "me: $(ME)"
	sudo chown $(ME):$(ME) -R .

lint:
	pipenv run pylint
	pipenv run mypy
	pipenv run flake8

build:
	docker compose build

drop:
	docker compose down -v

up:
	docker compose up --remove-orphans --build \
		code_review__web \
		code_review__celery \
		code_review__celery_beat

create_super_user:
	docker compose run code_review__web python manage.py createsuperuser

db__upgrade:
	docker compose run code_review__web python manage.py makemigrations
	docker compose run code_review__web python manage.py migrate
