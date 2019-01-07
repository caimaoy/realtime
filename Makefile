.PHONY: docs cover
test:
	# This runs all of the tests, on both Python 2 and Python 3.
	detox

cover:
	python -m pytest --verbose --cov-report html:cov.html --cov=realtime tests/