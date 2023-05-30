#!/bin/bash
# Script para probar la aplicación web.

if ! type -P flask &> /dev/null
then
	printf "The Flask framework isn't installed.\n" >&2
	printf "Install the following dependencies:\n" >&2
	printf "> pip install flask flask-wtf python-dotenv\n" >&2
	exit 1
fi

export FLASK_APP=logos.py
flask run --debug
