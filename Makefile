.PHONY: install test tox build install-package clean pre-commit-install pre-commit help

# Install pipenv
install-pipenv:
	pip install pipenv

# Activate shell
activate-shell:
	pipenv shell

# Install dependencies
install:
	pipenv install --dev

# Run tests with pytest
test:
	pipenv run pytest -m unit_test

# Run tests with tox
tox:
	pipenv run tox

# Build package
build:
	pipenv run python setup.py sdist bdist_wheel

# Install package
install-package:
	pipenv run pip install dist/*.whl

# Generate new key
generate-key:
	pipenv run python cli.py --mode generate_key

# Encrypt sensitive data file
encrypt:
	pipenv run python cli.py --mode encrypt --key "$(security_key)" --data_file "configs/test/common.yml"

# Decrypt sensitive data file
decrypt:
	pipenv run python cli.py --mode decrypt --key "$(security_key)" --data_file "configs/test/common.yml"

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

help:
	@echo "Available targets:"
	@echo "  install-pipenv         Install pipenv"
	@echo "  activate-shell         Activate pipenv shell"
	@echo "  install                Install dependencies"
	@echo "  test                   Run tests with pytest"
	@echo "  tox                    Run tests with tox"
	@echo "  build                  Build package"
	@echo "  install-package        Install package"
	@echo "  generate-key           Generate new key"
	@echo "  encrypt                Encrypt sensitive data file"
	@echo "  decrypt                Decrypt sensitive data file"
	@echo "  clean                  Clean up"
	@echo "  pre-commit-install     Install pre-commit hooks"
	@echo "  pre-commit             Run pre-commit hooks"
	@echo "  help                   Show this help message"
