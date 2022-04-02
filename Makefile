#!/bin/bash
init:
	pipenv install --dev
	npm install --include=dev
	npx webpack
	pipenv run python ./manage.py migrate
	pipenv run python ./manage.py createsuperuser

pre_commit:
	pipenv run pre-commit run --all-files

make_migrate:
	pipenv run python ./manage.py makemigrations
	pipenv run python ./manage.py migrate
