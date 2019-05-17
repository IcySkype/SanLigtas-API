from flask import request
from flask_restplus import Resource

from ..util.dto import UserAdminDto, PasswordAdminDto
from ..util.decoratoradmin import token_required
<<<<<<< HEAD
from ..service.useradmin_service import save_new_user, get_all_users, get_a_user, delete_user, update_user, update_password, search_by_user
=======
from ..service.useradmin_service import save_new_user, get_all_users, get_a_user, delete_user, update_user, update_password, search_by_username, search_by_fullname, search_by_public_id, search_by_role
>>>>>>> a4a50f6df42b7c12e2eac01c26aadccccbb04cc3

api = UserAdminDto.api
_user = UserAdminDto.user
parser= UserAdminDto.parser
parser2 = PasswordAdminDto.parser

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
		# user = get_a_user(public_id)
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
		data = request.form
		user = update_password(public_id, data)
		if not user:
			api.abort(404)
		else:
			return user
			
<<<<<<< HEAD
@api.route('/search/<search_user>')			
=======
@api.route('/search/by_username/<searchterm_user>')			
>>>>>>> a4a50f6df42b7c12e2eac01c26aadccccbb04cc3
class SearchByUsername(Resource):
	@api.doc('search by username, name, public_id, role')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_user, envelope='data')
	def get(self, search_user):
		results = search_by_user(search_user)
		return results

<<<<<<< HEAD
=======
@api.route('/search/by_name/<searchterm_name>')			
class SearchByName(Resource):		
	@api.doc('search by name')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_user, envelope='data')
	def get(self, searchterm_name):
		results = search_by_fullname(searchterm_name)
		return results

@api.route('/search/by_id/<searchterm_id>')			
class SearchByPublicId(Resource):
	@api.doc('search by public id')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_user, envelope='data')
	def get(self, searchterm_id):
		results = search_by_public_id(searchterm_id)
		return results
		
@api.route('/search/by_role/<searchterm_role>')			
class SearchByRole(Resource):
	@api.doc('search by admin role')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_user, envelope='data')
	def get(self, searchterm_role):
		results = search_by_role(searchterm_role)
		return results
#Search 'Main Admin' to search for main admins, 'relief admin' for relief admins, 'social worker admin' for socil worker admins
#All search functions are case insensitive. you can search for 'Main' or 'maiN' or 'MaIn', same result.
>>>>>>> a4a50f6df42b7c12e2eac01c26aadccccbb04cc3
