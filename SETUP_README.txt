REMEMBER TO CHANGE THE DATABASE URI(postgres_local_base) ON APP\MAIN\CONFIG.PY TO MATCH YOUR LOCAL DATABASE.
THE FORMAT FOR THE LOCAL URI IS: 'postgresql://USERNAME:PASSWORD@localhost:5432/DATABASE'

LINUX/UNIX:
make install : installs both system-packages and python-packages
make clean : cleans up the app
make tests : runs the all the tests
make run : starts the application
make all : performs clean-up,installation , run tests , and starts the app.

WINDOWS:
1. install python 3
	python 3 already includes pip on installation
   run 'pip install -r requirements.txt'
2. to run tests: 'py manage.py test'
3. to run the api: 'py manage.py run'

AFTER INSTALLING SYSTEM AND PYTHON PACKAGES, REMEMBER TO MIGRATE AND UPGRADE YOUR DATABASE
migrate: 'py manage.py db migrate'
upgrade: 'py manage.py db upgrade'