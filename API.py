from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from passlib.apps import custom_app_context as pwd_context

#No db yet.
db_connect = create_engine('postgresql://postgres:postgres@localhost:5432/SLDB')
app = Flask(__name__)
api = Api(app)


class User(db.Model):
	#attributes
	__tablename__ = 'Users'
	id = db.Column('user_id', db.Integer())
	username = db.Column('username', db.String())
	pass_hash = db.Column('pass', db.String())

	#methods
	def __init__(self, attributes):
		self.attributes setup

	def hash_pass(self, pass):
		self.pass_hash = pwd_context.encrypt(pass)

	def verify_pass(self, pass):
		return pwd_context.verify(pass, self.pass_hash)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def get_id(self):
		return unicode(self.id)

class User_Name(Resource):
	def get(self, id):
		query = User.query.filter_by(id=id)
		result = {'data': [dict(zip(tuple(query.keys()),i)) for i in query]}
		return jsonify(result)

api.add_resource(User_Name, '/user/<id>')

@app_route("/")
def hello():
	return jsonify({'hello world'})

@login_manager.user_loader
def load_user(id)
	reg_user = User.query.filter_by(id=id).first()
	return reg_user

if __name__ == '__main__'
	app.run(debug=True)