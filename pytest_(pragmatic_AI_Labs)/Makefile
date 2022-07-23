install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting \
		--cov=smath --cov=web --cov=cli tests
	python -m pytest --nbval notebook.ipynb
	#python -m pytest -v tests/test_web.py  # just to test web

format:
	black *.py

debug:
	python -m pytest -vv --pdb  # Debugger is inovked

debug_three:
	python -m pytest -vv --pdb --maxfail=3

one_test:
	python -m pytest -vv tests/test_greeting.py::test_my_name4

lint:
	pylint --disable=R,C *.py

all: install lint test format