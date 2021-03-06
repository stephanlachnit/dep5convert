# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: CC0-1.0

.PHONY: default
default: egg_info

## build tagerts

.PHONY: egg_info
egg_info:
	python3 setup.py egg_info

.PHONY: docs
docs: egg_info
	make -C docs html

.PHONY: build
build:
	python3 -m build

## lint targets

.PHONY: lint
lint: flake8 pylint reuse

.PHONY: flake8
flake8:
	python3 -m flake8 src/dep5convert tests setup.py docs/source/conf.py

.PHONY: pylint
pylint:
	python3 -m pylint src/dep5convert tests setup.py docs/source/conf.py

.PHONY: reuse
reuse:
	python3 -m reuse lint

## test targets

.PHONY: test
test: pytest

.PHONY: pytest
pytest: egg_info
	python3 -m pytest

## misc tagets

.PHONY: clean
clean:
	python3 -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
	python3 -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('*.egg-info')]"
	python3 -Bc "import shutil; shutil.rmtree('.pytest_cache', ignore_errors=True)"
	python3 -Bc "import shutil; shutil.rmtree('dist', ignore_errors=True)"
	make -C docs clean
