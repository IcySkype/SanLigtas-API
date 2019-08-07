from flask import request
from flask_restplus import Resource

from ..util.dto import HouseDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.household_service import save_new_house, get_all_houses, get_a_house, delete_house

api = HouseDto.api
_house = HouseDto.household
parser= HouseDto.parser


parse_auth = api.parser()
parse_auth.add_argument('Authorization', type=str, help='Auth', location='headers')

@api.route('/')
class HouseList(Resource):
	@api.doc('list of registered households',parser=parse_auth)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_house, envelope='data')
	def get(self):
		return get_all_houses()

	@api.doc('create a new household', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@api.response(201, 'Household successfully created.')
	@token_required
	def post(self):
		data = request.form
		print (data)
		return save_new_house(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The House identifier')
@api.response(404, 'Household not found.')
class Evacuees(Resource):
	@api.doc('get a house',parser=parse_auth)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_house)
	def get(self, public_id):
		house = get_a_house(public_id)
		if not house:
			api.abort(404)
		else:
			return house
	
	@api.doc('delete an evacuee',parser=parse_auth)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, public_id):
		house = delete_house(public_id)
		if not house:
			api.abort(404)
		else:
			return house

