all: mutants

.PHONY: all check clean coverage format install linter mutants tests

module = mean_differences_mc
codecov_token = a786f529-2c0a-4f0a-b711-11cdbf362b10

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests

clean:
	rm --force --recursive .pytest_cache
	rm --force --recursive ${module}.egg-info
	rm --force --recursive $$(find . -name "__pycache__")
	rm --force .coverage
	rm --force .mutmut-cache

coverage:
	pytest --cov=${module} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${module}
	black --line-length 100 tests

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants:
	mutmut run --paths-to-mutate ${module}

tests:
	pytest --verbose
