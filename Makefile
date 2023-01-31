SHELL = /bin/bash

VIRTUALENV_DIR := .venv

help:
	@echo "See the sources"


setup:
	python3 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate
	pip install -r requirements.txt


get-presentation:
	set -e
	. $(VIRTUALENV_DIR)/bin/activate
	python main.py





	