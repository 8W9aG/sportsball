#!/bin/sh

set -e

git push origin main
rm -rf dist
python -m build
twine upload --skip-existing dist/* --verbose
