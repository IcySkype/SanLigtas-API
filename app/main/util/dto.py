from flask_restplus import Namespace, fields


class UserAdminDto:
	api = Namespace('useradmin', description='User related operations')
	user = api.model('useradmin', {
		'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'role': fields.String(required=True, description='user role'),
        'gender': fields.String(required=True, description='user gender'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
	parser = api.parser()
	parser.add_argument('email', type=str, help='User Email Address', location='form')
	parser.add_argument('username', type=str, help='User Username', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')
	parser.add_argument('first_name', type=str, help='User First Name', location='form')
	parser.add_argument('last_name', type=str, help='User Last Name', location='form')
	parser.add_argument('role', type=str, help='User Role', location='form')
	parser.add_argument('gender', type=str, help='User Gender', location='form')
	

class PasswordAdminDto:
	api = Namespace('useradmin', description='User password operation')
	user = api.model('useradmin', {
		'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
		})
	parser = api.parser()
	parser.add_argument('email', type=str, help='User Email', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')


class PasswordMobileDto:
	api = Namespace('usermobile', description='User password operation')
	user = api.model('usermobile', {
		'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
		})
	parser = api.parser()
	parser.add_argument('email', type=str, help='User Email', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')

	

class UserMobileDto:
	api = Namespace('usermobile', description='User related operations')
	user = api.model('usermobile', {
		'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'birth_date': fields.String(required=True, description='user birth date'),
        'gender': fields.String(required=True, description='user gender'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        'address': fields.String(required=True, description='user address'),
        'contact_number': fields.String(required=True, description='user contact number'),

    })
	parser = api.parser()
	parser.add_argument('email', type=str, help='User Email Address', location='form')
	parser.add_argument('first_name', type=str, help='User Furst Name', location='form')
	parser.add_argument('last_name', type=str, help='User Last Name', location='form')
	parser.add_argument('username', type=str, help='User Username', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')
	parser.add_argument('first_name', type=str, help='User First Name', location='form')
	parser.add_argument('last_name', type=str, help='User Last Name', location='form')
	parser.add_argument('birth_date', type=str, help='User Birth Date', location='form')
	parser.add_argument('gender', type=str, help='User Gender', location='form')
	parser.add_argument('contact_number', type=str, help='User Contact Number', location='form')
	parser.add_argument('address', type=str, help='User Address', location='form')

class AuthAdminDto:
	api = Namespace('authadmin', description='Authentication related operations')
	user_auth = api.model('auth_details',{
		'email' : fields.String(required=True, description='The Email Address'),
		'password' : fields.String(required=True, description='The User Password')
	})
	parser = api.parser()
	parser.add_argument('email', type=str, help='The Email Address', location='form')
	parser.add_argument('password', type=str, help='The User Password', location='form')


class AuthMobileDto:
	api = Namespace('authmobile', description='Authentication related operations')
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
		'capacity' : fields.Integer(required=True, description='Distribution Center Capacity'),
		'public_id' : fields.String(description='Distribution Center Public Id')
	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Distribution Center Name')
	parser.add_argument('address', type=str, help='Physical Address of the Distribution Center')
	parser.add_argument('capacity', type=int, help='Distribution Center Capacity')

class EvacueesDto:
	api = Namespace('evacuees', description='Evacuees related operations')
	evacuees = api.model('evacuees',{
		'name' : fields.String(required=True, description='Evacuees Name'),
		'home_id' : fields.Integer(required=True, description='Evacuees home_id'),
		'address' : fields.String(required=True, description='Evacuees address'),
		'date_of_reg' : fields.String(required=True, description='Evacuees date of regristration'),
		'gender' : fields.String(required=True, description='Evacuees gender'),
		'age' : fields.Integer(required=True, description='Evacueesr age'),
		'religion' : fields.String(required=True, description='Evacuees religion'),
		'civil_status' : fields.String(required=True, description='Evacuees civil_status'),
		'educ_attainment' : fields.String(required=True, description='Evacuees educ_attainment'),
		'occupation' : fields.String(required=True, description='Evacuees occupation')


	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Evacuees Name')
	parser.add_argument('home_id', type=int, help='Evacuees home_id')
	parser.add_argument('address', type=str, help='Evacuees address')
	parser.add_argument('date_of_reg', type=str, help='Evacuees date of regristration')
	parser.add_argument('gender', type=str, help='Evacuees gender')
	parser.add_argument('age', type=int, help='Evacuees age')
	parser.add_argument('religion', type=str, help='Evacuees religion')
	parser.add_argument('civil_status', type=str, help='Evacuees civil_status')
	parser.add_argument('educ_attainment', type=str, help='Evacuees educ_attainment')
	parser.add_argument('occupation', type=str, help='Evacuees occupation')	