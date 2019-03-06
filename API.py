from config import app
from flask import request
from flask_jsonpify import jsonify
from flask_restful import reqparse, abort, Resource
from json import dumps
from Models import *
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import create_engine

#parser = reqparse.RequestParser()
#parser.add_argument

@app_route("/", methods=['GET'])
def home():
	return jsonify([{'text':'hello world'}])

@app_route("/api/v1/users", method=['GET'])
def get_users():
	userlist = User.query.all()
	return jsonify(json_list=[i.serialize for i in userlist])

"""
Testing using flask_restful.
class Users(Resource):
	def get(self):
		userlist = User.query.all()
		return jsonify(json_list=[i.serialize for i in userlist])
	
	def post(self):
		args = parser. 
"""
@login_manager.user_loader
def load_user(id):
	reg_user = User.query.filter_by(id=id).first()
	return reg_user

if __name__ == '__main__':
	app.run(debug=True)