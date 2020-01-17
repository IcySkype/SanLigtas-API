from flask_restplus import Namespace, fields, inputs

class UserDto:
	api = Namespace('user', description='User related operations')
	user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'first_name': fields.String(required=True, description='user first name'),
		'middle_name': fields.String(description='user middle name'),
        'last_name': fields.String(required=True, description='user last name'),
        'role_id': fields.Integer(required=True, description='user role'),
        'gender': fields.String(required=True, description='user gender'),
        'public_id': fields.String(description='user Identifier')
    })

	parser = api.parser()
	parser.add_argument('username', type=str, help='User Username', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')
	parser.add_argument('first_name', type=str, help='User First Name', location='form')
	parser.add_argument('middle_name', type=str, help='User Middle Name', location='form')
	parser.add_argument('last_name', type=str, help='User Last Name', location='form')
	parser.add_argument('role_id', type=int, help='User Role', location='form')
	parser.add_argument('gender', type=str, help='User Gender', location='form')
	parser.add_argument('Authorization', type=str, help='Auth', location='headers')
	

class PasswordDto:
	api = Namespace('useradmin', description='User password operation')
	user = api.model('useradmin', {
		'username': fields.String(required=True, description='user email address'),
        'old_pass': fields.String(required=True, description='current user password'),
		'new_pass': fields.String(required=True, description='new user password')
		})
	parser = api.parser()
	parser.add_argument('username', type=str, help='User Username', location='form')
	parser.add_argument('old_pass', type=str, help='Current Password', location='form')
	parser.add_argument('new_pass', type=str, help='New Password', location='form')
	parser.add_argument('Authorization', location='headers')

class AuthDto:
	api = Namespace('authadmin', description='Authentication related operations')
	user_auth = api.model('auth_details',{
		'username' : fields.String(required=True, description='Username'),
		'password' : fields.String(required=True, description='Password')
	})
	parser = api.parser()
	parser.add_argument('username', type=str, help='Username', location='form')
	parser.add_argument('password', type=str, help='Password', location='form')

class DistCenterDto:
	api = Namespace('distcenter', description='Distribution Center related operations')
	distcenter = api.model('distcenter',{
		'name' : fields.String(required=True, description='Distribution Center Name'),
		'barangay_id' : fields.Integer(required=True, description='Physical Address of the Distribution Center'),
		'capacity' : fields.Integer(required=True, description='Distribution Center Capacity'),
		'public_id' : fields.String(description='Distribution Center Public Id')
	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Distribution Center Name', location='form')
	parser.add_argument('barangay_id', type=str, help='Physical Address of the Distribution Center', location='form')
	parser.add_argument('capacity', type=int, help='Distribution Center Capacity', location='form')
	parser.add_argument('Authorization', location='headers')


class EvacueesDto:
	api = Namespace('evacuees', description='Evacuees related operations')
	evacuees = api.model('evacuees',{
		'first_name' : fields.String(required=True, description='Evacuees First Name'),
		'middle_name' : fields.String(required=True, description='Evacuees Middle Name'),
		'last_name' : fields.String(required=True, description='Evacuees Last Name'),
		'age' : fields.Integer(required=True, description='Evacueesr age'),
		'gender' : fields.String(required=True, description='Evacuees gender'),
		'religion' : fields.String(required=True, description='Evacuees religion'),
		'civil_status' : fields.String(required=True, description='Evacuees civil_status'),
		'public_id' : fields.String(description='Evacuees Public Id'),
		'family_id' : fields.String(description='Family Public Id'),
		'barangay_id' : fields.Integer(description='Barangay Id')
	})

	parser = api.parser()
	parser.add_argument('first_name', type=str, help='Evacuees First Name', location='form')
	parser.add_argument('middle_name', type=str, help='Evacuees Middle Name', location='form')
	parser.add_argument('last_name', type=str, help='Evacuees Last Name', location='form')
	parser.add_argument('age', type=int, help='Evacuees age', location='form')
	parser.add_argument('gender', type=str, help='Evacuees gender', location='form')
	parser.add_argument('religion', type=str, help='Evacuees religion', location='form')
	parser.add_argument('civil_status', type=str, help='Evacuees civil_status', location='form')
	parser.add_argument('family_id', type=str, help='family public id', location='form')
	parser.add_argument('barangay_id', type=int, help='barangy id', location='form')
	parser.add_argument('Authorization', location='headers')

class FamilyDto:
	api = Namespace('family', description='Family related operations')
	family = api.model('household',{
		'name' : fields.String(required=True, description='Name of the Family'),
		'public_id' : fields.String(description='Family Public Id')
	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Name of the Family, eg. "Smith-Rogers"', location='form')
	parser.add_argument('Authorization', location='headers')
	
class AnnounceDto:
	api = Namespace('announcement', description='Announcement related operations')
	announce = api.model('announcement',{
		'title' : fields.String(required=True, description='Announcement Title'),
		'details' : fields.String(required=False, description='Announcement Details'),
		'type' : fields.Integer(description='Announcement Type'),
		'public_id' : fields.String(description='Public Id'),
		'post_date' : fields.String(required=False, description='Post Date'),
		'last_edit_date' : fields.String(required=False, description='Last Edit Date'),
		'isActive' : fields.Boolean(description='Announcement isActive')
	})
	parser = api.parser()
	parser.add_argument('title', type=str, help='Announcement Title', location='form')
	parser.add_argument('details', type=str, help='Announcement Detail', location='form')
	parser.add_argument('type', type=int, help='Announcement Type', location='form')
	parser.add_argument('Authorization', location='headers')
	
class ManageCenterDto:
	api = Namespace('manage', description='Center managing related operations')
	managecenter = api.model('manage_center',{
		'admin_id' : fields.String(required=True),
		'center_id': fields.String(required=True)
	})
	parser = api.parser()
	parser.add_argument('admin_id', type=str, location='form')
	parser.add_argument('center_id', type=str, location='form')
	parser.add_argument('Authorization', location='headers')
	
class RegisterToCenterDto:
	api = Namespace('register', description='Evacuee registering related operations')
	managecenter = api.model('register',{
		'evacuee_id' : fields.String(required=True),
		'center_id': fields.String(required=True)
	})
	parser = api.parser()
	parser.add_argument('evacuee_id', type=str, location='form')
	parser.add_argument('center_id', type=str, location='form')
	parser.add_argument('Authorization', location='headers')


class RGoodsDto:
	api = Namespace('rgoods', description='Relief Goods related operations')
	rgoods = api.model('rgoods',{
		'name' : fields.String(required=True, description='Relief Goods Name'),
		'details' : fields.String(required=False, description='Relief Goods Details'),
		'public_id': fields.String(required=True, description='Relief Goods Identifier'),
		'type': fields.Integer(required=True, description='Relief Goods Type'),
		'amount': fields.Integer(required=True, description='Relief Goods Amount'),
		'received_date': fields.Date(required=True, description='Date goods received'),
		'distribute_date': fields.Date(required=False, description='Date goods distributed'),
		'status': fields.String(required=False, description='Relief Goods Status'),
		'isActive': fields.Boolean(description='Relief Goods Active status'),
		'center_id': fields.String(required=True, description='Distribution Center where goods are stored/distributed.'),
	})

	parser = api.parser()
	parser.add_argument('name', type=str, location='form')
	parser.add_argument('details', type=str, location='form')
	parser.add_argument('type', type=int, location='form')
	parser.add_argument('amount', type=int, location='form')
	parser.add_argument('status', type=str, location='form')
	parser.add_argument('center_id', type=str, location='form')
	parser.add_argument('Authorization', location='headers')