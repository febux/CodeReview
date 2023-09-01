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
		code_review__celery_beat \
		code_review__db_exporter

db__create_super_user:
	docker compose up -d code_review__db
	docker compose build code_review__manager_db
	sleep 5
	docker compose run --rm code_review__manager_db python manage.py createsuperuser

db__flush:
	docker compose up -d code_review__db
	docker compose build code_review__manager_db
	sleep 5
	docker compose run --rm code_review__manager_db python manage.py flush --noinput
	docker compose run --rm code_review__manager_db python manage.py migrate --fake code_review__app zero

db__migrate:
	docker compose up -d code_review__db
	docker compose build code_review__manager_db
	sleep 5
	docker compose run --rm code_review__manager_db python manage.py migrate
