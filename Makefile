.PHONY: quality

setup:
	cp .env.example .env
	pipenv install

security:
	pipenv check

formatting:
	pipenv run isort -rc src
	pipenv run autoflake --in-place --remove-all-unused-imports -r src
	pipenv run black src

linting:
	pipenv run pylint src/*

typing:
	pipenv run mypy src

test:
	pipenv run pytest

quality: security formatting linting typing test
