from flask_restplus import Namespace, fields


class UserDto:
	api = Namespace('user', description='User related operations')
	user = api.model('user', {
		'email' : fields.String(required=True, description='User Email Address'),
		'username' : fields.String(required=True, description='User Username'),
		'password': fields.String(required=True, description='User Password'),
		'public_id' : fields.String(description='User Identifier')
	})
	parser = api.parser()
	parser.add_argument('email', type=str, help='User Email Address', location='form')
	parser.add_argument('username', type=str, help='User Username', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')

class AuthDto:
	api = Namespace('auth', description='Authentication related operations')
	user_auth = api.model('auth_details',{
		'email' : fields.String(required=True, description='The Email Address'),
		'password' : fields.String(required=True, description='The User Password')
	})
	parser = api.parser()
	parser.add_argument('email', type=str, help='The Email Address', location='form')
	parser.add_argument('password', type=str, help='The User Password', location='form')

class DistCenterDto:
	api = Namespace('distcenter', description='Distribution Center related operations')
	distcenter = api.model('distcenter',{
		'name' : fields.String(required=True, description='Distribution Center Name'),
		'address' : fields.String(required=True, description='Physical Address of the Distribution Center'),
		'capacity' : fields.Integer(required=True, description='Distribution Center Capacity')
	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Distribution Center Name')
	parser.add_argument('address', type=str, help='Physical Address of the Distribution Center')
	parser.add_argument('capacity', type=int, help='Distribution Center Capacity')