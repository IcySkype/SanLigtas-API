from flask import request
from flask_restplus import Resource

from ..util.dto import EvacueesDto, AssignedEvacueeDto, FemaleAgeRangeDto
from ..util.decoratoradmin import token_required, admin_token_required
from ..service.evacuees_service import save_new_evacuees, female_age_range, male_age_range, get_age_female, get_age_male, get_all_evacuees, get_a_evacuee, delete_evacuees, update_evacuees, add_evacuee, search_evacuee, get_center_center_id

api = EvacueesDto.api
_evacuees = EvacueesDto.evacuees
parser= EvacueesDto.parser
parser2 = AssignedEvacueeDto.parser
parser3 = FemaleAgeRangeDto.parser


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
	@token_required
	def post(self):
		#create new evacuees
		data = request.form
		print (data)
		return save_new_evacuees(data=data)




@api.route('/assign/evacuee')			
class AssignEvacuee(Resource):
	@api.doc('Assign an evacuee in a center', parser=parser2)
	@api.response(201, 'Evacuee successfully assigned.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def put(self):
		data = request.form
		print(data)
		return add_evacuee(data=data)





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
		evacuees = get_a_evacuee(home_id)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees
	
	@api.doc('delete an evacuees')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def delete(self, home_id):
		evacuees = delete_evacuees(home_id)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees

	@api.doc('update a evacuees', parser=parser)
	@api.response(201, 'evacuees Succesfully Updated.')
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def put(self, home_id):
		data = request.form
		evacuees = update_evacuees(home_id, data)
		if not evacuees:
			api.abort(404)
		else:
			return evacuees



@api.route('/search/<search_term>')			
class SearchByUsername(Resource):
	@api.doc('search by Name, Address, Gender')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_evacuees, envelope='data')
	def get(self, search_term):
		results = search_evacuee(search_term)
		return results


@api.route('/get/center/<center_id>')			
class SearchByUsername(Resource):
	@api.doc('Get center by center ID')
	@api.response(200, 'Results found.')
	@api.marshal_list_with(_evacuees, envelope='data')
	def get(self, center_id):
		results = get_center_center_id(center_id)
		return results

			
			
@api.route('/age_female')			
class FemaleAge(Resource):
	@api.doc('Get age female')
	@api.response(200, 'Results found.')
	def get(self):
		
		return get_age_female()


@api.route('/age_female/<range_age>')
class FemaleAgeAdd(Resource):
	@api.doc('Add female range', parser=parser3)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def put(self, range_age):
		return female_age_range(range_age)

			
@api.route('/age_male')			
class FemaleAge(Resource):
	@api.doc('Get age male')
	@api.response(200, 'Results found.')
	def get(self):
		
		return get_age_male()


@api.route('/age_male/<range_age>')
class FemaleAgeAdd(Resource):
	@api.doc('Add male range', parser=parser3)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@admin_token_required
	def put(self, range_age):
		return male_age_range(range_age)

			
			
