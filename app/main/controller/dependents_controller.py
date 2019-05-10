from flask import request
from flask_restplus import Resource

from ..util.dto import DependentsDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.dependents_service import save_new_dependents, get_all_dependents, get_a_dependents, delete_dependents, update_dependents

api = DependentsDto.api
_dependents = DependentsDto.dependents
parser= DependentsDto.parser


@api.route('/')
class DependentsList(Resource):
	@api.doc('list_of_registered_dependents')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_dependents, envelope='data')
	def get(self):
		#return registered user list
		return get_all_dependents()

	@api.response(201, 'Dependents successfully created.')
	@api.doc('create a new dependents', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self):
		data = request.form
		print (data)
		return save_new_dependents(data=data)

@api.route('/<dependents_id>')
@api.param('dependents_id', 'The Dependents identifier')
@api.response(404, 'Dependents not found.')
class Evacuees(Resource):
	@api.doc('get a dependents')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_dependents)
	def get(self, dependents_id):
		evacuees = get_a_evacuee(dependents_id)
		if not dependents:
			api.abort(404)
		else:
			return dependents
	
	@api.doc('delete an dependents')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, dependents_id):
		dependents = get_a_dependents(dependents_id)
		if not dependents:
			api.abort(404)
		else:
			return dependents

	@api.doc('update a dependents', parser=parser)
	@api.response(201, 'dependents Succesfully Updated.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def put(self, dependents_id):
		evacuees = get_a_dependents(dependents_id)
		data = request.form
		evacuees = update_dependents(dependents_id, data)
		if not dependents:
			api.abort(404)
		else:
			return dependents
