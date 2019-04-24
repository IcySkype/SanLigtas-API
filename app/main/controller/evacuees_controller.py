from flask import request
from flask_restplus import Resource

from ..util.dto import EvacueesDto
from ..util.decorator import token_required, admin_token_required
from ..service.evacuees_service import save_new_evacuees, get_all_evacuees, get_a_evacuee, delete_evacuees, update_evacuees

api = EvacueesDto.api
_evacuees = EvacueesDto.evacuees
parser= EvacueesDto.parser


@api.route('/')
class EvacueesList(Resource):
	@api.doc('list_of_registered_evacuues')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_evacuees, envelope='data')
	def get(self):
		#return registered user list
		return get_all_evacuees()

	@api.response(201, 'Evacuees successfully created.')
	@api.doc('create a new evacuees', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def post(self):
		#create new evacuees
		data = request.form
		print (data)
		return save_new_evacuees(data=data)

@api.route('/<home_id>')
@api.param('home_id', 'The Evacuee identifier')
@api.response(404, 'Evacuee not found.')
class Evacuees(Resource):
	@api.doc('get a evacuees')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_evacuees)
	def get(self, home_id):
		#gets a specific user with public_id
		user = get_a_evacuee(home_id)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees
	
	@api.doc('delete a evacuees')
	@api.response(204, 'Evacuees Succesfully Deleted.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, home_id):
		#delete a specific user with public_id
		user = get_a_evacuee(home_id)
		if not evacuees:
			api.abort(404)
		else:
			return delete_evacuees(evacuees)

	@api.doc('update a evacuees', parser=parser)
	@api.response(201, 'evacuees Succesfully Updated.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def put(self, home_id):
		user = get_a_evacuee(home_id)
		data = request.form
		user = update_evacuees(home_id, data)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees