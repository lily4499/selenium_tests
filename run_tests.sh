#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt
# Create directory for test reports
mkdir -p test-reports
# Run tests and generate a JUnit XML report for Jenkins
pytest --junitxml=test-reports/results.xml test_ui.py