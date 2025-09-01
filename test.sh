#!/bin/sh

set -e

PYTEST_CURRENT_TEST=1 pytest -n auto --capture=no --cov-report=term --cov=sportsball tests
coverage html -d coverage_html
