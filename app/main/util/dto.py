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
	parser.add_argument('Authorization', type=str, help='Auth', location='headers')
	

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
	parser.add_argument('username', type=str, help='User Username', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')
	parser.add_argument('first_name', type=str, help='User First Name', location='form')
	parser.add_argument('last_name', type=str, help='User Last Name', location='form')
	parser.add_argument('birth_date', type=str, help='User Birth Date', location='form')
	parser.add_argument('gender', type=str, help='User Gender', location='form')
	parser.add_argument('contact_number', type=str, help='User Contact Number', location='form')
	parser.add_argument('address', type=str, help='User Address', location='form')
	parser.add_argument('Authorization', type=str, help='Auth', location='headers')

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
		'public_id' : fields.String(description='Distribution Center Public Id'),
		'latitude' : fields.String(description='Distribution Center Latitude'),
		'longitude' : fields.String(description='Distribution Center Longitude'),
		'id' : fields.String(description='Distribution Center Marker')
	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Distribution Center Name', location='form')
	parser.add_argument('address', type=str, help='Physical Address of the Distribution Center', location='form')
	parser.add_argument('capacity', type=int, help='Distribution Center Capacity', location='form')
	parser.add_argument('latitude', type=int, help='Distribution Center Latitude')
	parser.add_argument('longitude', type=int, help='Distribution Center Longitude')
	parser.add_argument('id', type=int, help='Distribution Center Marker')
	parser.add_argument('Authorization', type=str, help='Auth', location='headers')



class AssignedCenterDto:
	api = Namespace('assignedcenter', description='Assigning admin in a Center')
	assignedcenter = api.model('assignedcenter', {
		'center_public_id': fields.String(required=True, description='Center Public ID'),
		'center_admin': fields.String(required=True, description='Assigned Admin'),
		})
	parser = api.parser()
	parser.add_argument('center_public_id', type=str, help='Center Public ID', location='form')
	parser.add_argument('center_admin', type=str, help='Center Admin' , location='form')
	parser.add_argument('Authorization', type=str, help='Auth', location='headers')



class AssignedEvacueeDto:
	api = Namespace('evacuees', description='Assigning evacuee in a Center')
	evacuees = api.model('evacuees', {
		'center_id': fields.Integer(description='Center ID'),
		'home_id': fields.Integer(description='Evacuees home ID')
		})
	parser = api.parser()
	parser.add_argument('center_id', type=int, help='Center ID', location='form')
	parser.add_argument('home_id', type=int, help='Evacuees home ID', location='form')
	parser.add_argument('Authorization', type=str, help='Auth', location='headers')




class EvacueesDto:
	api = Namespace('evacuees', description='Evacuees related operations')
	evacuees = api.model('evacuees',{
		'name' : fields.String(required=True, description='Evacuees Name'),
		'home_id' : fields.Integer(required=True, description='Evacuees home_id'),
		'address' : fields.String(required=True, description='Evacuees address'),
		'gender' : fields.String(required=True, description='Evacuees gender'),
		'age' : fields.Integer(required=True, description='Evacueesr age'),
		'religion' : fields.String(required=True, description='Evacuees religion'),
		'civil_status' : fields.String(required=True, description='Evacuees civil_status'),
		'educ_attainment' : fields.String(required=True, description='Evacuees educ_attainment'),
		'occupation' : fields.String(required=True, description='Evacuees occupation')


	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Evacuees Name', location='form')
	parser.add_argument('home_id', type=int, help='Evacuees home_id', location='form')
	parser.add_argument('address', type=str, help='Evacuees address', location='form')
	parser.add_argument('gender', type=str, help='Evacuees gender', location='form')
	parser.add_argument('age', type=int, help='Evacuees age', location='form')
	parser.add_argument('religion', type=str, help='Evacuees religion', location='form')
	parser.add_argument('civil_status', type=str, help='Evacuees civil_status', location='form')
	parser.add_argument('educ_attainment', type=str, help='Evacuees educ_attainment', location='form')
	parser.add_argument('occupation', type=str, help='Evacuees occupation', location='form')
	parser.add_argument('Authorization', location='headers')


class DependentsDto:
	api = Namespace('dependents', description='Dependents related operations')
	dependents = api.model('dependents',{
		'name' : fields.String(required=True, description='Dependents Name'),
		'dependents_id' : fields.String(required=True, description='Dependents ID'),
		'home_id' : fields.Integer(required=True, description='Dependents home ID'),
		'address' : fields.String(required=True, description='Dependents address'),
		'gender' : fields.String(required=True, description='Dependents gender'),
		'age' : fields.Integer(required=True, description='Dependents age'),
		'educ_attainment' : fields.String(required=True, description='Dependents educ_attainment'),
		'occupation' : fields.String(required=True, description='Dependents occupation')


	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Dependents Name', location='form')
	parser.add_argument('dependents_id', type=str, help='Dependents ID')
	parser.add_argument('home_id', type=int, help='Dependents home id', location='form')
	parser.add_argument('address', type=str, help='Dependents address', location='form')
	parser.add_argument('gender', type=str, help='Dependents gender', location='form')
	parser.add_argument('age', type=int, help='Dependents age', location='form')
	parser.add_argument('educ_attainment', type=str, help='Dependents educ_attainment', location='form')
	parser.add_argument('occupation', type=str, help='Dependents occupation', location='form')
	parser.add_argument('Authorization', type=str, help='Auth', location='headers')