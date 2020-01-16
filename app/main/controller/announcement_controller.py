from flask import request
from flask_restplus import Resource

from ..util.dto import AnnounceDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.announcement_service import create_announcement, get_announcement_board, get_announcement, deactivate_announcement, update_announcement

api = AnnounceDto.api
_announcement = AnnounceDto.announce
parser= AnnounceDto.parser

@api.route('/')
class AnnounceBoard(Resource):
	@api.doc('list of announcements',parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_announcement, envelope='data')
	def get(self):
		return get_announcement_board()

	@api.doc('post new announcement', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@api.response(201, 'Announcement Posted.')
	@token_required
	def post(self):
		data = request.form
		return create_announcement(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The House identifier')
@api.response(404, 'No such announcement posted.')
class Announcement(Resource):
	@api.doc('get announcement')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_announcement)
	def get(self, public_id):
		ann = get_announcement(public_id)
		if not ann:
			api.abort(404)
		else:
			return ann
	
	@api.doc('Deactivate Announcement')
	@api.response(204, 'Announcement Deactivated')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, public_id):
		ann = get_announcement(public_id)
		if not ann:
			api.abort(404)
		else:
			return deactivate_announcement(public_id)


	@api.doc('update announcement', parser=parser)
	@api.response(201, 'Announcement Updated.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def put(self, public_id):
		data = request.form
		ann = update_announcement(public_id, data)
		if not ann:
			api.abort(404)
		else:
			return ann
	


