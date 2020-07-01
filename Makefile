clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log
	@echo 'Temporary files deleted'

lint: clean
	@printf '\n --- \n >>> Running linter...<<<\n'
	@pylint --rcfile=.pylintrc  ./*
	@printf '\n FINISHED! \n --- \n'

style:
	@isort -m 3 -tc -y
	@black -S -t py37 -l 79 ./. --exclude '/(\.git|\.venv|env|venv|build|dist)/'

requirements-pip:
	@pip install --upgrade pip
	@pip install -r requirements.txt

new-pattern:
	@mkdir ./$(name)
	@touch ./$(name)/implementation.py
	@echo "import implementation" > ./$(name)/__init__.py
	@touch ./$(name)/README.md

test: clean
	pytest -s -vvv

test-matching: clean  ## Run only tests matching pattern. E.g.: make test-matching test=TestClassName
	py.test -k $(test) -s -vvv