install:
	poetry install

run:
	poetry run wats

lint:
	poetry run flake8 wats
