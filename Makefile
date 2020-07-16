.PHONY: clean format lint matants tests

repo = mean_differences_mc
codecov_token = a786f529-2c0a-4f0a-b711-11cdbf362b10

clean:
	rm --force --recursive $$(find . -name "__pycache__")
	rm --force --recursive .pytest_cache
	rm --force .coverage
	rm --force .mutmut-cache

format:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests

lint:
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests
	pylint ${repo}
	pylint tests

mutants:
	mutmut run --paths-to-mutate mean_differences_mc 

tests:
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}
