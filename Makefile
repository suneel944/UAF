.PHONY: upgrade-pip install-pre-commit run-pre-commit tox tox-env build install-wheel clean help test generate-key encrypt decrypt pre-commit-install

# Variables
TOX_ENV_NAME = py3119 # default environment name
PACKAGE_NAME =

# Upgrade pip
upgrade-pip:
	@echo "Upgrading pip..."
	@pip install --upgrade pip

# Run tests with pytest
test:
	@echo "Running tests with pytest..."
	@pytest -m unit_test

# Run tox with specified Python version
tox:
	@echo "Running tox for Python version $(PYTHON_VERSION)..."
	@if [ -z "$(PYTHON_VERSION)" ]; then \
		echo "Error: PYTHON_VERSION is not set. Supported versions: 3114, 3115, 3116, 3117, 3118, 3119."; \
		exit 1; \
	fi
	@case $(PYTHON_VERSION) in \
		3114|3115|3116|3117|3118|3119) tox -e py$(PYTHON_VERSION) ;; \
		*) echo "Error: Unsupported PYTHON_VERSION. Supported versions: 3114, 3115, 3116, 3117, 3118, 3119."; exit 1 ;; \
	esac

# Build package
build:
	@echo "Building package..."
	@python -m build --wheel --outdir dist

# Install package from wheel
install-wheel:
	@echo "Installing package..."
	@pip install dist/*.whl --force-reinstall

# Generate new key
generate-key:
	@echo "Generating new key..."
	@python cli.py --mode generate_key

# Encrypt sensitive data file
encrypt:
	@echo "Encrypting sensitive data file..."
	@python cli.py --mode encrypt --key "$(security_key)" --data_file "configs/test/common.yml"

# Decrypt sensitive data file
decrypt:
	@echo "Decrypting sensitive data file..."
	@python cli.py --mode decrypt --key "$(security_key)" --data_file "configs/test/common.yml"

# Install pre-commit hooks
install-pre-commit:
	@echo "Installing pre-commit hooks..."
	@pre-commit install

# Run pre-commit hooks
run-pre-commit:
	@echo "Running pre-commit hooks..."
	@pre-commit run --all-files || ( echo "Pre-commit checks failed"; exit 1 )

# Clean up
clean:
	@echo "Cleaning up..."
	@rm -rf .pytest_cache .tox dist build .mypy_cache *.egg-info
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete

# Helper section
help:
	@echo "Available targets:"
	@echo "  upgrade-pip        - Upgrade pip"
	@echo "  test               - Run tests with pytest"
	@echo "  tox                - Run tox with specified Python version"
	@echo "  build              - Build package"
	@echo "  install-wheel      - Install wheel"
	@echo "  generate-key       - Generate new key"
	@echo "  encrypt            - Encrypt sensitive data file"
	@echo "  decrypt            - Decrypt sensitive data file"
	@echo "  install-pre-commit - Install pre-commit hooks"
	@echo "  run-pre-commit     - Run pre-commit hooks"
	@echo "  clean              - Clean up"
	@echo "  help               - Show this help message"
