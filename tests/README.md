# Tests for Stock Analysis Tool

This folder contains unit tests and integration tests for the Stock Analysis and Trading Recommendation Tool.

## Test Structure

The test suite is organized to mirror the structure of the `src/` directory:

- `test_data.py` - Tests for data fetching and transaction history
- `test_analysis.py` - Tests for technical analysis and predictions
- `test_visualization.py` - Tests for charting functions
- `test_utils.py` - Tests for utility functions
- `test_integration.py` - End-to-end integration tests

## Running Tests

### Running All Tests
```bash
# From the project root directory
pytest

# With detailed output
pytest -v
```

### Running Specific Test Categories
```bash
# Run only data tests
pytest tests/test_data.py

# Run only analysis tests
pytest tests/test_analysis.py

# Run tests matching a pattern
pytest -k "Technical"
```

### Code Coverage
```bash
# Run tests with coverage
pytest --cov=src

# Generate detailed coverage report
pytest --cov=src --cov-report=html
```

### Test Markers

We use pytest markers to categorize tests:

```bash
# Run only slow tests
pytest -m slow

# Run tests that require API access
pytest -m api

# Skip slow tests
pytest -m "not slow"
```

## Continuous Integration

Tests are automatically run on GitHub Actions when code is pushed to the main branch. Check `.github/workflows/python-tests.yml` for the configuration.

## Menulis Tests Baru

Saat membuat tests baru:
1. Ikuti konvensi penamaan `test_*.py` untuk file tests
2. Gunakan fixtures untuk data berulang
3. Isolasi dependencies dengan mocks
4. Pastikan membuat assertions yang jelas
5. Tulis docstrings untuk fungsi test

## Continuous Integration

Tests secara otomatis dijalankan dalam GitHub Actions workflow ketika:
- Pull request dibuat ke branch main
- Push ke branch main dilakukan

Lihat `.github/workflows/python-tests.yml` untuk detail konfigurasi.
