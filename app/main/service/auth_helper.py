from app.main.model.user import UserAdmin, UserMobile
from ..service.blacklist_service import save_token


class AuthAdmin:
	@staticmethod
	def login_user(data):
		try:
			#fetch user data
			user = UserAdmin.query.filter_by(email=data.get('email')).first()
			if user and user.check_password(data.get('password')):
				role = str(data.get('role'))
				isAdmin = "admin" in role
				if not isAdmin:
					response_object = {
						'status' : 'fail',
						'message' : 'User not an admin'
					}
					return response_object, 401
				auth_token = user.encode_auth_token(user.id)
				username = user.username
				first_name = user.first_name
				last_name = user.last_name
				if auth_token:
					response_object = {
						'status' : 'success',
						'message' : 'Logged in successfully!',
						'Authorization' : auth_token.decode(),
						'first_name': first_name,
						'last_name' : last_name,
						'username' : username
					}
					return response_object, 200
			else:
				response_object = {
					'status' : 'fail',
					'message' : 'Login failed. Check email or password.'
				}
				return response_object, 401
		except Exception as e:
			print(e)
			response_object = {
				'status' : 'fail',
				'message' : 'Try again'
			}
			return response_object, 500

	@staticmethod
	def logout_user(auth_token):#data
		#if data:
			#auth_token = data.split(" ")[1]
		#else:
			#auth_token = ''
		if auth_token:
			resp = UserAdmin.decode_auth_token(auth_token)
			if not isinstance(resp, str):
				#blacklist auth_token so that user can't use it anymore
				return save_token(token=auth_token)
			else:
				response_object = {
				'status' : 'fail',
				'message' : resp
				}
				return response_object, 401
		else:
			response_object = {
				'status' : 'fail',
				'message' : 'Auth token was invalid'
			}
			return response_object, 403

	@staticmethod
	def get_logged_in_user(new_request):
		#get auth token
		auth_token = new_request.headers.get('Authorization')
		if auth_token:
			resp = UserAdmin.decode_auth_token(auth_token)
			if not isinstance(resp, str):
				user = UserAdmin.query.filter_by(id=resp).first()
				response_object = {
					'status' : 'success',
					'data' : {
						'user_id' : user.id,
						'email' : user.email,
						'role' : user.role,
						'registered_on' : str(user.registered_on)
					}
				}
				return response_object, 200
			response_object = {
					'status' : 'fail',
					'message' : resp
			}
			return response_object, 401
		else:
			response_object = {
					'status' : 'fail',
					'message' : 'Invalid auth token'
			}
			return response_object, 401


class AuthMobile:
	@staticmethod
	def login_user(data):
		try:
			#fetch user data
			user = UserMobile.query.filter_by(email=data.get('email')).first()

			if user and user.check_password(data.get('password')):
				auth_token = user.encode_auth_token(user.id)
				username = user.username
				first_name = user.first_name
				last_name = user.last_name
				if auth_token:
					response_object = {
						'status' : 'success',
						'message' : 'Logged in successfully!',
						'Authorization' : auth_token.decode(),
						'first_name': first_name,
						'last_name' : last_name,
						'username' : username
					}
					return response_object, 200
			else:
				response_object = {
					'status' : 'fail',
					'message' : 'Login failed. Check email or password.'
				}
				return response_object, 401
		except Exception as e:
			print(e)
			response_object = {
				'status' : 'fail',
				'message' : 'Try again'
			}
			return response_object, 500

	@staticmethod
	def logout_user(auth_token):#data
		#if data:
			#auth_token = data.split(" ")[1]
		#else:
			#auth_token = ''
		if auth_token:
			resp = UserAdmin.decode_auth_token(auth_token)
			if not isinstance(resp, str):
				#blacklist auth_token so that user can't use it anymore
				return save_token(token=auth_token)
			else:
				response_object = {
				'status' : 'fail',
				'message' : resp
				}
				return response_object, 401
		else:
			response_object = {
				'status' : 'fail',
				'message' : 'Auth token was invalid'
			}
			return response_object, 403

	@staticmethod
	def get_logged_in_user(new_request):
		#get auth token
		auth_token = new_request.headers.get('Authorization')
		if auth_token:
			resp = UserAdmin.decode_auth_token(auth_token)
			if not isinstance(resp, str):
				user = UserAdmin.query.filter_by(id=resp).first()
				response_object = {
					'status' : 'success',
					'data' : {
						'user_id' : user.id,
						'email' : user.email,
						'registered_on' : str(user.registered_on)
					}
				}
				return response_object, 200
			response_object = {
					'status' : 'fail',
					'message' : resp
			}
			return response_object, 401
		else:
			response_object = {
					'status' : 'fail',
					'message' : 'Invalid auth token'
			}
			return response_object, 401


class AuthMobile:
	@staticmethod
	def login_user(data):
		try:
			#fetch user data
			user = UserMobile.query.filter_by(email=data.get('email')).first()
			if user and user.check_password(data.get('password')):
				auth_token = user.encode_auth_token(user.id)
				if auth_token:
					response_object = {
						'status' : 'success',
						'message' : 'Logged in successfully!',
						'Authorization' : auth_token.decode()
					}
					return response_object, 200
			else:
				response_object = {
					'status' : 'fail',
					'message' : 'Login failed. Check email or password.'
				}
				return response_object, 401
		except Exception as e:
			print(e)
			response_object = {
				'status' : 'fail',
				'message' : 'Try again'
			}
			return response_object, 500

	@staticmethod
	def logout_user(auth_token):#data
		#if data:
			#auth_token = data.split(" ")[1]
		#else:
			#auth_token = ''
		if auth_token:
			resp = UserMobile.decode_auth_token(auth_token)
			if not isinstance(resp, str):
				#blacklist auth_token so that user can't use it anymore
				return save_token(token=auth_token)
			else:
				response_object = {
				'status' : 'fail',
				'message' : resp
				}
				return response_object, 401
		else:
			response_object = {
				'status' : 'fail',
				'message' : 'Auth token was invalid'
			}
			return response_object, 403

	@staticmethod
	def get_logged_in_user(new_request):
		#get auth token
		auth_token = new_request.headers.get('Authorization')
		if auth_token:
			resp = UserMobile.decode_auth_token(auth_token)
			if not isinstance(resp, str):
				user = UserMobile.query.filter_by(id=resp).first()
				print(user)
				response_object = {
					'status' : 'success',
					'data' : {
						'user_id' : user.id,
						'email' : user.email,
						'registered_on' : str(user.registered_on)
					}
				}
				return response_object, 200
			response_object = {
					'status' : 'fail',
					'message' : resp
			}
			return response_object, 401
		else:
			response_object = {
					'status' : 'fail',
					'message' : 'Invalid auth token'
			}
			return response_object, 401