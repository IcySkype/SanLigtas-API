from flask import request
from flask_restplus import Resource

from ..util.dto import FamilyDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.evacuees_service import get_family, get_all_families, create_family, edit_family, delete_family, search_family

api = FamilyDto.api
_family = FamilyDto.family
parser= FamilyDto.parser

@api.route('/')
class FamilyList(Resource):
	@api.doc('list_of_registered_families')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_family, envelope='data')
	def get(self):
		return get_all_families()

	@api.doc('create a new family', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@api.response(201, 'Family successfully created.')
	@token_required
	def post(self):
		data = request.form
		print (data)
		return create_family(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The family identifier')
@api.response(404, 'Family not found.')
class Family(Resource):
	@api.doc('get specific family',parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_family)
	def get(self, public_id):
		family = get_family(public_id)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees
	
	@api.doc('delete a family (non cascade)',parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, public_id):
		evacuees = delete_family(public_id)
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
		evacuees = edit_family(public_id, data)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees
			
			
@api.route('/search/<searchterm_name>')			
class SearchByName(Resource):
	@api.doc('search by name')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_family, envelope='data')
	def get(self, searchterm_name):
		results = search_family(searchterm_name)
		return results
