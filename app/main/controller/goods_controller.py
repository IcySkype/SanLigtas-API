from flask import request
from flask_restplus import Resource

from ..util.dto import RGoodsDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.goods_service import save_new_rgoods, get_all_rgoods, get_rgoods, update_rgoods, delete_rgoods, distribute, search_center, search_code

api = RGoodsDto.api
_rgoods = RGoodsDto.rgoods
parser = RGoodsDto.parser


@api.route('/')
class RGoodsList(Resource):
	@api.doc('list_of_all_relief_goods')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_rgoods, envelope='data')
	def get(self):
		return get_all_rgoods()
  
	
	@api.doc('add new relief goods', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@api.response(201, 'Relief Goods successfully created.')
	@admin_token_required
	def post(self):
		data = request.form
		return save_new_rgoods(data=data)


@api.route('/<code>')
@api.param('code', 'Relief Goods Code')
@api.response(404, 'Relief Goods not found.')
class DistCenter(Resource):
	@api.doc('get relief goods')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	@api.marshal_list_with(_rgoods)
	def get(self, code):
		rgoods = get_rgoods(code)
		if not rgoods:
			api.abort(404)
		else:
			return rgoods


	@api.doc('delete relief goods')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def delete(self, code):
		rgoods = delete_rgoods(code)
		if not rgoods:
			api.abort(404)
		else:
			return rgoods


	@api.doc('update relief goods', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def put(self, code):
		data = request.form
		rgoods = update_rgoods(code=code, data=data)
		if not rgoods:
			api.abort(404)
		else:
			return rgoods

			
@api.route('/search/<searchterm>')			
class SearchByCenter(Resource):
	@api.doc('search by distribution center')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_rgoods, envelope='data')
	def get(self, searchterm):
		print(searchterm)
		results = search_center(searchterm)
		return results
