from functools import wraps
from flask import request

from app.main.service.auth_helper import AuthMobile


def token_required(f):
	@wraps(f)
	def  decorated(*args, **kwargs):
		
		data, status = AuthMobile.get_logged_in_user(request)
		token = data.get('data')

		if not token:
			return data, status

		return f(*args, **kwargs)

	return decorated


def admin_token_required(f):
	@wraps(f)
	def  decorated(*args, **kwargs):
		
		data, status = AuthMobile.get_logged_in_user(request)
		token = data.get('data')

		if not token:
			return data, status

		role = token.get('role')#token.get('role')
		if role < 1:#if not admin:
			response_object = {
				'status' : 'fail',
				'message' : 'admin token required'
			}
			return response_object, 401

		return f(*args, **kwargs)
	return decorated

def admin2_token_required(f):
	@wraps(f)
	def  decorated(*args, **kwargs):
		
		data, status = Auth.get_logged_in_user(request)
		token = data.get('data')

		if not token:
			return data, status

		role = token.get('role')#token.get('role')
		if role < 2:#if not admin:
			response_object = {
				'status' : 'fail',
				'message' : 'admin token required'
			}
			return response_object, 401

		return f(*args, **kwargs)

	return decorated

def main_admin_token_required(f):
	@wraps(f)
	def  decorated(*args, **kwargs):
		
		data, status = Auth.get_logged_in_user(request)
		token = data.get('data')

		if not token:
			return data, status

		role = token.get('role')#token.get('role')
		if role < 3:#if not admin:
			response_object = {
				'status' : 'fail',
				'message' : 'admin token required'
			}
			return response_object, 401

		return f(*args, **kwargs)

	return decorated
