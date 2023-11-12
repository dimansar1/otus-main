test:
	pytest homework_10/homework_05/test.py
coverage:
	pytest -s --cov --cov-report html --cov-fail-under 96 homework_10/homework_05/test.py