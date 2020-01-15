from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth
from app.main.service.user_service import check_role


def token_required(f):
	@wraps(f)
	def  decorated(*args, **kwargs):
		
		data, status = AuthAdmin.get_logged_in_user(request)
		token = data.get('data')

		if not token:
			return data, status

		return f(*args, **kwargs)

	return decorated


def admin_token_required(f):
	@wraps(f)
	def  decorated(*args, **kwargs):
		
		data, status = Auth.get_logged_in_user(request)
		token = data.get('data')

		if not token:
			return data, status
		
		role = token.get('role')
		
		if check_role(role) != 'Social Worker' or check_role(role) != 'Admin':
			response_object = {
				'status' : 'fail',
				'message' : 'admin token required'
			}
			return response_object, 401

		return f(*args, **kwargs)

	return decorated
