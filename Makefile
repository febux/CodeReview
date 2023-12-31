SHELL := /bin/bash
CWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ME := $(shell whoami)

nothing:
	@echo "do nothing"

clean_up:
	docker system prune -a
	docker volume prune -a

fix_permissions:
	@echo "me: $(ME)"
	sudo chown $(ME):$(ME) -R .

lint:
	poetry run ruff ./src
	poetry run mypy

build:
	docker-compose build

drop:
	docker-compose down -v

up__dev:
	docker-compose up --remove-orphans --build \
		code_review__db \
		code_review__redis \
		code_review__web \
		code_review__celery \
		code_review__celery_beat

up__prod:
	docker-compose -f docker-compose.prod.yml up --remove-orphans --build \
		code_review__db \
		code_review__balancer \
		code_review__redis \
		code_review__web \
		code_review__celery \
		code_review__celery_beat

up_background__prod:
	docker-compose -f docker-compose.prod.yml up -d --remove-orphans --build \
		code_review__db \
		code_review__balancer \
		code_review__redis \
		code_review__web \
		code_review__celery \
		code_review__celery_beat

up_background__dev:
	docker-compose up -d --remove-orphans --build \
		code_review__db \
		code_review__redis \
		code_review__web \
		code_review__celery \
		code_review__celery_beat

db__create_super_user:
	docker-compose up -d code_review__db
	docker-compose build code_review__manager_db
	sleep 5
	docker-compose run --rm code_review__manager_db python manage.py createsuperuser

db__flush:
	docker-compose up -d code_review__db
	docker-compose build code_review__manager_db
	sleep 5
	docker-compose run --rm code_review__manager_db python manage.py flush --noinput

db__make_migrations:
	docker-compose up -d code_review__db
	docker-compose build code_review__manager_db
	sleep 5
	docker-compose run --rm code_review__manager_db python manage.py makemigrations

db__migrate:
	docker-compose up -d code_review__db
	docker-compose build code_review__manager_db
	sleep 5
	docker-compose run --rm code_review__manager_db python manage.py migrate
