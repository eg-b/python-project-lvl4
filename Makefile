run:
	poetry run python ./manage.py runserver

run_gunicorn:
	export DJANGO_SETTINGS_MODULE=task_manager.settings
	poetry run gunicorn hello_django.wsgi

heroku_push:
	git push heroku main

scale:
	heroku ps:scale web=1

configure:
	poetry install

lint:
	poetry run flake8 task_manager

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

test:
	poetry run pytest --cov=task_manager tests/ --cov-report xml

translate:
	cd task_manager; django-admin makemessages -l ru; django-admin compilemessages

migrate:
	poetry run python manage.py migrate