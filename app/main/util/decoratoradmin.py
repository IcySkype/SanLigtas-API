from functools import wraps
from flask import request

from app.main.service.auth_helper import AuthAdmin


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
		
		data, status = AuthAdmin.get_logged_in_user(request)
		token = data.get('data')
		print(token)

		if not token:
			return data, status
		
		admin = token.get('role')
		print (admin)
		if not admin:
			response_object = {
				'status' : 'fail',
				'message' : 'admin token required'
			}
			return response_object, 401

		return f(*args, **kwargs)

	return decorated
