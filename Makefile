day1:
	python.exe -m Day1.sortAndSubstract

venv:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt


.PHONY: day1
