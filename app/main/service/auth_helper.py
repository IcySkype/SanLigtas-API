from app.main.model.user import Account
from ..service.blacklist_service import save_token


class Auth:
	@staticmethod
	def login_user(data):
		try:
			#fetch user data
			user = Account.query.filter_by(username=data.get('username')).first()
			#if user exists + correct password + user is active, login
			if user and user.check_password(data.get('password')) and user.isActive:
				auth_token = user.encode_auth_token(user.id)
				if auth_token:
					response_object = {
						'status' : 'success',
						'message' : 'Logged in successfully!',
						'Authorization' : auth_token.decode(),
					}
					return response_object, 200
			else:
				response_object = {
					'status' : 'fail',
					'message' : 'Login failed. Check username or password.'
				}
				return response_object, 401
		except Exception as e:
			print(e)
			response_object = {
				'status' : 'fail',
				'message' : 'Unknown error. Try again'
			}
			return response_object, 500

	@staticmethod
	def logout_user(auth_token):#data
		#if data:
			#auth_token = data.split(" ")[1]
		#else:
			#auth_token = ''
		if auth_token:
			resp = Account.decode_auth_token(auth_token)
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
			resp = Account.decode_auth_token(auth_token)
			if not isinstance(resp, str):
				user = Account.query.filter_by(id=resp).first()
				user_d = Account.query.filter_by(public_id=user.public_id).first()
				response_object = {
					'status' : 'success',
					'data' : {
						'user_id' : user.id,
						'username' : user.username,
						'first_name' : user.first_name,
						'last_name' : user.last_name,
						'role' : user.role,
						'registered_on' : str(user_d.registered_on)
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
