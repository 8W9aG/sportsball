#!/bin/sh

set -e

echo "Formatting..."
echo "--- Ruff ---"
ruff format sportsball
echo "--- isort ---"
isort sportsball

echo "Checking..."
#echo "--- Flake8 ---"
#flake8 sportsball
#echo "--- pylint ---"
#pylint sportsball
echo "--- mypy ---"
mypy sportsball
echo "--- Ruff ---"
ruff check sportsball
echo "--- pyright ---"
pyright sportsball
