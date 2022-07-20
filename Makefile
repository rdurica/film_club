#!/bin/bash
init:
	poetry install
	npm install --include=dev
	npx webpack
	poetry run python ./manage.py migrate
	poetry run python ./manage.py loaddata app/core/fixtures/labels.json

pre_commit:
	poetry run pre-commit run --all-files

make_migrate:
	poetry run python ./manage.py makemigrations
	poetry run python ./manage.py migrate

webpack:
	npx webpack --watch

process_movies:
	poetry run python ./manage.py process_movies