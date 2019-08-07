import os
#postgres_local_base = 'postgresql://ewxybuxwluzggk:d0df279a43db226dd3b8b9a8bade3e6e68c0700d21b3f953fa00a182dc6936eb@ec2-54-235-208-103.compute-1.amazonaws.com:5432/d8from30f48hfj'
postgres_local_base = 'postgresql://postgres:postgres@localhost:5432/SanLigDB'
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