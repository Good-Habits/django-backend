.PHONY: quality

setup:
	cp .env.example .env
	pipenv install

quality:
	pipenv check
	pipenv run black src
	pipenv run pylint src/*
	pipenv run mypy src
	pipenv run pytest
