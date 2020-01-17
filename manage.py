import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist, distcenter, evacuees

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

from app.main.service.user_service import role_init
from app.main.service.distcenter_service import brgy_init
from app.main.service.announcement_service import type_init
from app.main.service.goods_service import type_init as init_goodtype
@manager.command
def init():
	print("Initializing default values.")
	role_init()
	brgy_init()
	type_init()
	init_goodtype()
	print("Default values loaded into database.")
	

@manager.command
def run():
	app.run()

@manager.command
def test():
	tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

if __name__ == '__main__':
	manager.run()
