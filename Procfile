release: python manage.py db upgrade
heroku-postbuild : python manage.py init
web : gunicorn manage:app