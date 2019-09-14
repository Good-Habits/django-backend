# "Good Habits" backend code written in Django

![](https://github.com/Good-Habits/django-backend/.github/workflows/python-app.yml/badge.svg)

> A Django backend for an app

## Development

### Git Hooks

Precommit hooks allow developers to create clean commits and restrict pushing
changes to the repository without running tests first.

For managing pre-commit and pre-push hooks we are using
the [pre-commit](https://pre-commit.com/) package.
The configuration is stored in this [configuration file](./pre-commit-config.yaml).

To install it run `pre-commit install -f -t pre-commit -t pre-push`

To test out hooks run `pre-commit run --all-files`
