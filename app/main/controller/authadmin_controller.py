from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import AuthAdmin
from ..util.dto import AuthAdminDto
from ..util.decoratoradmin import token_required

api = AuthAdminDto.api
user_auth = AuthAdminDto.user_auth
parser = AuthAdminDto.parser


@api.route('/login')
class UserLogin(Resource):
	@api.doc('user login', parser=parser)
	def post(self):
		post_data = request.form
		return AuthAdmin.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
	@api.doc('logout a user')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self):
		auth_header = request.headers.get('Authorization')
		return AuthAdmin.logout_user(auth_token=auth_header)
