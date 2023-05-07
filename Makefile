# Makefile for pytest automation framework with pipenv and pre-commit

.PHONY: install test tox build install-package clean pre-commit-install pre-commit help

# Install pipenv
install-pipenv:
	pip install pipenv

# Activate shell
activate-shell:
	pipenv shell

# Install dependencies
install:
	pipenv install --skip-lock

# Run tests with pytest
test:
	pipenv run pytest

# Run tests with tox
tox:
	pipenv run tox

# Build package
build:
	pipenv run python setup.py sdist bdist_wheel

# Install package
install-package:
	pipenv run pip install dist/*.whl

# Generae new key
generate-key:
	pipenv run python cli.py --mode generate_key

# Encrypt sensitive data file
encrypt:
	pipenv run python cli.py --mode decrypt --key ${{ secrets.SECURITY_KEY }} --data_file configs/test/common.yml

# Decrypt sensitive data file
decrypt:
	

# Clean up
clean:
	pipenv --rm
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf dist
	rm -rf build
	rm -rf .mypy_cache
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Install pre-commit hooks
pre-commit-install:
	pipenv run pre-commit install

# Run pre-commit hooks
pre-commit:
	pipenv run pre-commit run --all-files

