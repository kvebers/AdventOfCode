day1Part1:
	python.exe -m Day1.sortAndSubstract

day1Part2:
	python.exe -m Day1.sortAndMultiply


day2:
	python.exe -m Day2.isSafe

day3:
	python.exe -m Day3.task3

venv:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt


.PHONY: day1Part1 day1Part2 venv freeze day2 day3
