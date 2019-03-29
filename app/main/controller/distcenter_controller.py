from flask import request
from flask_restplus import Resource

from ..util.dto import DistCenterDto
from ..service.distcenter_service import save_new_dcenter, get_all_dcenters, get_a_dcenter, update_dcenter, delete_dcenter

api = DistCenterDto.api
_dcenter = DistCenterDto.distcenter


@api.route('/')
class UserList(Resource):
	@api.doc('list_of_registered_distribution_centers')
	@api.marshal_list_with(_dcenter, envelope='data')
	def get(self):
		return get_all_dcenters()

	@api.response(201, 'User successfully created.')
	@api.doc('add a new distribution center')
	@api.expect(_dcenter, validate=True)
	def post(self):
		data = request.json
		return save_new_dcenter(data=data)


@api.route('/dcenter/<id>')
@api.param('id', 'The Distribution Center ID')
@api.response(404, 'Distribution Center not found.')
class DistCenter(Resource):
	@api.doc('get a distribution center')
	@api.marshal_list_with(_dcenter)
	def get(self, id):
		dcenter = get_a_dcenter(id)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter


	@api.doc('delete a distribution center')
	@api.marshal_list_with(_dcenter)
	def delete(self, id):
		dcenter = delete_dcenter(id)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter


	@api.doc('update a distribution center')
	@api.expect(_dcenter, validate=True)
	@api.marshal_list_with(_dcenter)	
	def put(self, id):
		data = request.json
		dcenter = update_dcenter(id=id, data=data)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter