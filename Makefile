all: mutants

.PHONY: all clean format install lint mutants tests

module = mean_differences_mc
codecov_token = a786f529-2c0a-4f0a-b711-11cdbf362b10

clean:
	rm --force --recursive .pytest_cache
	rm --force --recursive ${module}.egg-info
	rm --force --recursive $$(find . -name "__pycache__")
	rm --force .coverage
	rm --force .mutmut-cache

format:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests

install:
	pip install --editable .

lint:
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests
	pylint \
        --disable=bad-continuation \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${module}
	pylint \
        --disable=bad-continuation \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        test

mutants:
	mutmut run --paths-to-mutate ${module}

tests:
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}
