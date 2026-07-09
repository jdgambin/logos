#!/bin/bash

set -e

if [ ! -d ".venv" ]; then
    echo "Virtual environment not found."
    echo "Create it with:"
    echo "python3 -m venv .venv"
    exit 1
fi

source .venv/bin/activate

if ! python -c "import flask, flask_wtf, sympy" &> /dev/null
then
    echo "Python dependencies are missing."
    echo "Install them with:"
    echo "pip install -r requirements.txt"
    exit 1
fi

if ! command -v latex &> /dev/null
then
    echo "LaTeX is not installed."
    echo "Install a LaTeX distribution and dvipng."
    exit 1
fi

export FLASK_APP=logos.py

flask run --debug