install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8

test:
	poetry run pytest
