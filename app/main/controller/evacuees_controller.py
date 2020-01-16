from flask import request
from flask_restplus import Resource

from ..util.dto import EvacueesDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.evacuees_service import save_new_evacuees, get_all_evacuees, get_an_evacuee, delete_evacuees, update_evacuees, search_by_name, stat_AgeVsGender

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
		return get_all_evacuees()
	
	@api.doc('create a new evacuees', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@api.response(201, 'Evacuees successfully created.')
	@token_required
	def post(self):
		data = request.form
		print (data)
		return save_new_evacuees(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The Evacuee identifier')
@api.response(404, 'Evacuee not found.')
class Evacuees(Resource):
	@api.doc('get an evacuees',parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_evacuees)
	def get(self, public_id):
		evacuees = get_an_evacuee(public_id)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees
	
	@api.doc('delete an evacuee',parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, public_id):
		evacuees = delete_evacuees(public_id)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees

	@api.doc('update a evacuee', parser=parser)
	@api.response(201, 'evacuees Succesfully Updated.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def put(self, public_id):
		evacuees = get_an_evacuee(public_id)
		data = request.form
		evacuees = update_evacuees(public_id, data)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees
			
			
@api.route('/search/<searchterm_name>')			
class SearchByName(Resource):
	@api.doc('search by name')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_evacuees, envelope='data')
	def get(self, searchterm_name):
		results = search_by_name(searchterm_name)
		return results

@api.route('/statistics/<gender>')			
class Stats(Resource):		
	@api.doc('statistics of ages')
	@api.response(200, 'Results found.')
	def get(self, gender):
		results = stat_AgeVsGender(gender)
		return results
