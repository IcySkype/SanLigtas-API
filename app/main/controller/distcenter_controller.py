from flask import request
from flask_restplus import Resource

from ..util.dto import DistCenterDto, ManageCenterDto, RegisterToCenterDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.distcenter_service import save_new_dcenter, get_all_sorted, get_a_dcenter, update_dcenter, delete_dcenter, search_center, manage, register

api = DistCenterDto.api
_dcenter = DistCenterDto.distcenter
parser = DistCenterDto.parser
manageparser = ManageCenterDto.parser
registerparser = RegisterToCenterDto.parser


@api.route('/')
class DCenterList(Resource):
	@api.doc('list_of_registered_distribution_centers')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_dcenter, envelope='data')
	def get(self):
		return get_all_sorted()
  
	@api.response(201, 'Center successfully created.')
	@api.doc('add a new distribution center', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def post(self):
		data = request.form
		return save_new_dcenter(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Distribution Center ID')
@api.response(404, 'Distribution Center not found.')
class DistCenter(Resource):
	@api.doc('get a distribution center')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_dcenter)
	def get(self, public_id):
		dcenter = get_a_dcenter(public_id)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter


	@api.doc('delete a distsribution center')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def delete(self, public_id):
		dcenter = delete_dcenter(public_id)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter


	@api.doc('update a distribution center', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def put(self, public_id):
		data = request.form
		dcenter = update_dcenter(public_id=public_id, data=data)
		if not dcenter:
			api.abort(404)
		else:
			return dcenter
			
@api.route('/search/<searchterm>')			
class SearchByName(Resource):
	@api.doc('search by name')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_dcenter, envelope='data')
	def get(self, searchterm):
		results = search_center(searchterm)
		return results

@api.route('/<public_id>/manage/<user_id>')
@api.param('public_id', 'The Distribution Center ID')
@api.param('user_id', 'Account ID')
class Manager(Resource):
	@api.doc('Assign manager', parser=manageparser)
	@api.response(200, 'Manager Added.')
	def post(self, public_id, user_id):
		return manage(public_id, user_id)
		
@api.route('/<public_id>/register/<evac_id>')
@api.param('public_id', 'The Distribution Center ID')
@api.param('evac_id', 'Evacuee ID')
class Register(Resource):
	@api.doc('Register evacuee to center', parser=registerparser)
	@api.response(200, 'Evacuee registered to center.')
	def post(self, public_id, evac_id):
		return register(public_id, evac_id)