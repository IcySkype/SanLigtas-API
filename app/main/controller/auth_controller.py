from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto
from ..util.decorator import token_required

api = AuthDto.api
user_auth = AuthDto.user_auth
parser = AuthDto.parser


@api.route('/login')
class UserLogin(Resource):
	@api.doc('user login', parser=parser)
	def post(self):
		post_data = request.form
		return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
	@api.doc('logout a user')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self):
		auth_header = request.headers.get('Authorization')
		return Auth.logout_user(auth_token=auth_header)
