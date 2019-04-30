from flask import request
from flask_restplus import Resource

from ..util.dto import UserMobileDto, PasswordMobileDto
from ..util.decoratormobile import token_required
from ..service.usermobile_service import save_new_user, get_all_users, get_a_user, delete_user, update_user, update_password

api = UserMobileDto.api
_user = UserMobileDto.user
parser= UserMobileDto.parser
parser2 = PasswordMobileDto.parser

#TODO: ADMIN mu add users
# lahi ra sya sa user mu register sa ilang selves
@api.route('/')
class UserList(Resource):
	@api.doc('list_of_registered_users')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_user, envelope='data')
	def get(self):
		#return registered user list
		return get_all_users()

	@api.response(201, 'User successfully created.')
	@api.doc('create a new user', parser=parser)
	def post(self):
		#create new user
		data = request.form
		return save_new_user(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
	@api.doc('get a user')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_user)
	def get(self, public_id):
		#gets a specific user with public_id
		user = get_a_user(public_id)
		if not user:
			api.abort(404)
		else:
			return user
	
	@api.doc('delete a user')
	@api.response(204, 'User Succesfully Deleted.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, public_id):
		#delete a specific user with public_id
		user = get_a_user(public_id)
		if not user:
			api.abort(404)
		else:
			return delete_user(user)

	@api.doc('update a user', parser=parser)
	@api.response(201, 'User Succesfully Updated.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def put(self, public_id):
		user = get_a_user(public_id)
		data = request.form
		user = update_user(public_id, data)
		if not user:
			api.abort(404)
		else:
			return user



@api.route('/password/<public_id>')
@api.response(404, 'User not found.')
class UserPassword(Resource):
	@api.doc('change password', parser=parser2)
	@api.response(201, 'Password successfully updated.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def put(self, public_id):
		user = get_a_user(public_id)
		print(user)
		data = request.form
		user = update_password(public_id, data)
		if not user:
			api.abort(404)
		else:
			return user