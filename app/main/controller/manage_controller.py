from flask import request
from flask_restplus import Resource

from app.main.service.manager_helper import ManageCenter
from ..util.dto import ManageCenterDto, DistCenterDto, UserAdminDto
from ..util.decoratoradmin import token_required

api = ManageCenterDto.api
parser = ManageCenterDto.parser
_dcenter = DistCenterDto.distcenter
_user = UserAdminDto.user

@api.route('/assign')
class AssignAdmin(Resource):
	@api.doc('Assign admin to center', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self):
		post_data = request.form
		admin_id = post_data.get('admin_id')
		center_id = post_data.get('center_id')
		return ManageCenter.assign_admin(admin_id=admin_id, dc_id=center_id)


@api.route('/unassign')
class UnassignAdmin(Resource):
	@api.doc('Unassign admin to center', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self):
		post_data = request.form
		admin_id = post_data.get('admin_id')
		center_id = post_data.get('center_id')
		return ManageCenter.unassign_admin(admin_id=admin_id, dc_id=center_id)
		
@api.route('/admin/<admin_id>')
class ViewManagedCenters(Resource):
	@api.doc('View centers managed by admin')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_dcenter, envelope='data')
	def get(self, admin_id):
		return ManageCenter.assigned_centers(admin_id)
		
@api.route('/center/<dc_id>')
class ViewManager(Resource):
	@api.doc('View who manages a specified center')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_user, envelope='data')
	def get(self, dc_id):
		return ManageCenter.manager_of(dc_id)