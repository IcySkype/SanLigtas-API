import os
postgres_local_base = 'postgres://veysrvdoempaeh:2befd9f1bc4d37fb44f4e48a18af75fac9e70b89cb31cc2a48b2d60bedb4ecd4@ec2-174-129-33-156.compute-1.amazonaws.com:5432/de8deb6hf9k9s5'
#postgres_local_base = 'postgresql://postgres:postgres@localhost:5432/sldb2'
#os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'super_secret_key')
	DEBUG = False

class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = postgres_local_base
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = postgres_local_base

config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY