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
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

publish:
	poetry publish -r testpypi

translate:
	cd task_manager; django-admin makemessages -l ru; django-admin compilemessages