from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import AuthMobile
from ..util.dto import AuthMobileDto
from ..util.decoratormobile import token_required

api = AuthMobileDto.api
user_auth = AuthMobileDto.user_auth
parser = AuthMobileDto.parser


@api.route('/login')
class UserLogin(Resource):
	@api.doc('user login', parser=parser)
	def post(self):
		post_data = request.form
		return AuthMobile.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
	@api.doc('logout a user')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self):
		auth_header = request.headers.get('Authorization')
		return AuthMobile.logout_user(auth_token=auth_header)
