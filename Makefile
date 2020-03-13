.PHONY: clean matation tests

mutation:
	mutmut run --paths-to-mutate mean_differences_mc 

tests:
	pytest --cov=mean_differences_mc --cov-report=term --verbose

clean:
	rm --force --recursive $$(find . -name "__pycache__")
	rm --force --recursive .pytest_cache
	rm --force .coverage
	rm --force .mutmut-cache