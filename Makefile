all: test

test: venv
	./venv/bin/pytest --junitxml=py-results1.xml

venv:
	virtualenv -p python3.8 venv
	./venv/bin/pip install -r requirements.txt
