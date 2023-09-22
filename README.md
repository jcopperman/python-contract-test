# Contract Testing in Python

This repository contains contract tests written in Python using [PyTest](https://pytest.org) for verifying the interactions between different services or components. Contract testing helps ensure that services adhere to predefined contracts or expectations.

## Installation

Before running the contract tests, make sure you have Python and the necessary dependencies installed. You can set up a virtual environment to isolate the project's dependencies:

```bash
python -m venv venv  # Create a virtual environment (optional)
venv\Scripts\activate  # Activate the virtual environment on Windows (use venv/bin/activate on macOS and Linux)
pip install -r requirements.txt  # Install project dependencies
```
## Running Contract Tests
```bash
pytest test_contract.py
```

This command will execute the test_contract function defined in test_contract.py and check if the interactions between services conform to the specified contracts.

## Dependencies

- [PyTest](https://pytest.org): Testing framework for Python.
- [requests](https://docs.python-requests.org): Library for making HTTP requests (if applicable).
