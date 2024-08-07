brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-prime:
	poetry run brain-prime

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl 

lint:
	flake8 brain_games

install:
	poetry install
