SHELL := /bin/bash
CWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ME := $(shell whoami)

nothing:
	@echo "do nothing"

build:
	docker compose build

drop:
	docker compose down -v

up:
	docker compose up --remove-orphans --build \
		code_review__web

create_super_user:
	docker compose run code_review__web python manage.py createsuperuser

