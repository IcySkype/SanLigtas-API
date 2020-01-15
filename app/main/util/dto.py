from flask_restplus import Namespace, fields, inputs



class UserDto:
	api = Namespace('user', description='User related operations')
	user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'first_name': fields.String(required=True, description='user first name'),
		'middle_name': fields.String(description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'role': fields.Integer(required=True, description='user role'),
        'gender': fields.String(required=True, description='user gender'),
        'public_id': fields.String(description='user Identifier')
    })

	parser = api.parser()
	parser.add_argument('username', type=str, help='User Username', location='form')
	parser.add_argument('password', type=str, help='User Password', location='form')
	parser.add_argument('first_name', type=str, help='User First Name', location='form')
	parser.add_argument('first_name', type=str, help='User Middle Name', location='form')
	parser.add_argument('last_name', type=str, help='User Last Name', location='form')
	parser.add_argument('role', type=int, help='User Role', location='form')
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

class DistCenterDto:
	api = Namespace('distcenter', description='Distribution Center related operations')
	distcenter = api.model('distcenter',{
		'name' : fields.String(required=True, description='Distribution Center Name'),
		'address' : fields.String(required=True, description='Physical Address of the Distribution Center'),
		'capacity' : fields.Integer(required=True, description='Distribution Center Capacity'),
		'public_id' : fields.String(description='Distribution Center Public Id')
	})
	parser = api.parser()
	parser.add_argument('name', type=str, help='Distribution Center Name', location='form')
	parser.add_argument('address', type=str, help='Physical Address of the Distribution Center', location='form')
	parser.add_argument('capacity', type=int, help='Distribution Center Capacity', location='form')
	parser.add_argument('Authorization', location='headers')


class EvacueesDto:
	api = Namespace('evacuees', description='Evacuees related operations')
	evacuees = api.model('evacuees',{
		'name' : fields.String(required=True, description='Evacuees Name'),
		'home_id' : fields.String(required=True, description='Evacuees home_id'),
		'is_house_leader' : fields.Boolean(required=True,description='Is evacuee leader of the household?'),
		'gender' : fields.String(required=True, description='Evacuees gender'),
		'age' : fields.Integer(required=True, description='Evacueesr age'),
		'religion' : fields.String(required=True, description='Evacuees religion'),
		'civil_status' : fields.String(required=True, description='Evacuees civil_status'),
		'educ_attainment' : fields.String(required=True, description='Evacuees educ_attainment'),
		'occupation' : fields.String(required=True, description='Evacuees occupation'),
		'public_id' : fields.String(description='Evacuees Public Id')
	})

	parser = api.parser()
	parser.add_argument('name', type=str, help='Evacuees Name', location='form')
	parser.add_argument('home_id', type=str, help='Evacuees home_id', location='form')
	parser.add_argument('is_house_leader', type=bool, help='Is evacuee leader of household?', location='form')
	parser.add_argument('gender', type=str, help='Evacuees gender', location='form')
	parser.add_argument('age', type=int, help='Evacuees age', location='form')
	parser.add_argument('religion', type=str, help='Evacuees religion', location='form')
	parser.add_argument('civil_status', type=str, help='Evacuees civil_status', location='form')
	parser.add_argument('educ_attainment', type=str, help='Evacuees educ_attainment', location='form')
	parser.add_argument('occupation', type=str, help='Evacuees occupation', location='form')
	parser.add_argument('Authorization', location='headers')

class HouseDto:
	api = Namespace('household', description='Household related operations')
	household = api.model('household',{
		'address' : fields.String(required=True, description='Physical Address of the Household'),
		'public_id' : fields.String(description='Household Public Id')
	})

	parser = api.parser()
	parser.add_argument('address', type=str, help='Physical Address of the Household', location='form')
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


class RGoodsDto:
	api = Namespace('rgoods', description='Center managing related operations')
	rgoods = api.model('rgoods',{
		'name' : fields.String(required=True, description='Relief Goods Name'),
		'code': fields.String(required=True, description='Relief Goods Code'),
		'type': fields.String(required=True, description='Relief Goods Type: Clothing|Consumable|Cash'),
		'status': fields.String(required=True, description='Relief Goods Status'),
		'amount': fields.Integer(required=True, description='Relief Goods Amount'),

		'center_id': fields.String(required=True, description='Distribution Center where goods are stored/distributed.'),
		'received_date': fields.Date(required=True, description='Date goods received'),
		'received_from': fields.String(required=True, description='Personnel recieving goods'),
		'distribute_date': fields.Date(required=False, description='Date goods distributed'),

		'expiry': fields.Date(required=False, description='Consumable Expiry Date'),
		'size': fields.String(required=False, description='Clothing Size'),
		'clothing_type': fields.String(required=False, description='Clothing Type: Upper|Lower|Headwear|Footwear|Underwear'),
		'condition': fields.String(required=False, description='Condition of clothes')
	})

	parser = api.parser()
	parser.add_argument('name', type=str, location='form')
	parser.add_argument('code', type=str, location='form')
	parser.add_argument('type', type=str, location='form')
	parser.add_argument('status', type=str, location='form')
	parser.add_argument('amount', type=int, location='form')

	parser.add_argument('center_id', type=str, location='form')
	parser.add_argument('received_date', type=inputs.date_from_iso8601, location='form')
	parser.add_argument('received_from', type=str, location='form')
	parser.add_argument('distribute_date', type=inputs.date_from_iso8601, location='form')

	parser.add_argument('expiry', type=inputs.date_from_iso8601, location='form')
	parser.add_argument('size', type=str, location='form')
	parser.add_argument('clothing_type', type=str, location='form')
	parser.add_argument('condition', type=str, location='form')

	parser.add_argument('Authorization', location='headers')