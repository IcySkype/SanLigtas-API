from flask_restplus import Namespace, fields


class UserDto:
	api = Namespace('user', description='User related operations')
	user = api.model('user', {
		'email' : fields.String(required=True, description='User Email Address'),
		'username' : fields.String(required=True, description='User Username'),
		'password': fields.String(required=True, description='User Password'),
		'public_id' : fields.String(description='User Identifier')
	})