black . --exclude=venv
isort -rc . --skip-glob="venv/**"
flake8 --max-line-length=88 --exclude=venv,build --extend-ignore="E203"
