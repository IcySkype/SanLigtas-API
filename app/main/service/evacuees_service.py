import datetime

from app.main import db
from app.main.model.evacuees import Evacuees


def save_new_evacuees(data):
	evacuees = Evacuees.query.filter_by(home_id=data['home_id']).first()
	if not evacuees:
		new_evacuees = Evacuees(
			name=data['name'],
			home_id=data['home_id'],
			date_of_reg=datetime.datetime.utcnow(),
			address=data['address'],
			gender=data['gender'],
			age=data['age'],
			religion=data['religion'],
			civil_status=data['civil_status'],
			educ_attainment=data['educ_attainment'],
			occupation=data['occupation']
		)
		print (new_evacuees) 
		save_changes(new_evacuees)
		response_object = {
			'status' : 'success',
			'message' : 'evacuees added'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'home id has been already used'
		}
		return response_object, 409


def get_all_evacuees():
	return Evacuees.query.all()


def get_a_evacuee(home_id):
	return Evacuees.query.filter_by(home_id=home_id).first()

def delete_evacuees(home_id):
	evacuees = Evacuees.query.filter_by(home_id=home_id).first()
	if evacuees:
			db.session.delete(evacuees)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'evacuees deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching evacuees found.'
		}
		return response_object, 409

def update_evacuees(home_id, data):

	evacuees = Evacuees.query.filter_by(home_id=home_id).first()
	otherEvacuees = Evacuees.query.filter(Evacuees.home_id != home_id).all()
	if evacuees:
		check_existing = False
		for x in otherEvacuees:
			if x.home_id == data['address']:
				check_existing = True
		if not check_existing:
			evacuees.name = data['name']
			evacuees.address = data['address'],
			evacuees.gender = data['gender'],
			evacuees.age = data['age'],
			evacuees.religion = data['religion'],
			evacuees.civil_status = data['civil_status'],
			evacuees.educ_attainment = data['educ_attainment'],
			evacuees.occupation = data['occupation']
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'distribution center updated'
			}
			return response_object, 200
		else:
			response_object = {
			'status' : 'fail',
			'message' : 'New Address already used.'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching distribution center found.'
		}
		return response_object, 409

def save_changes(data):
	db.session.add(data)
	db.session.commit()

# def update_evacuees(home_id, data):
# 	evacuees = Evacuees.query.filter_by(home_id=home_id).first()
# 	if evacuees:
# 		evacuees.home_id = data['home_id'],
#         evacuees.name = data['name']
#         evacuees.address = data['address']
#         evacuees.date_of_reg = data['date_of_reg'],
#         evacuees.gender = data['gender'],
#         evacuees.age = data['age'],
#         evacuees.religion = data['religion'],
#         evacuees.civil_status = data['civil_status'],
#         evacuees.educ_attainment = data['educ_attainment'],
#         evacuees.occupation = data['occupation']
#         db.session.commit()
#         response_object = {
#             'status': 'Success',
#             'message': 'evacuees updated.'
#         }
#         return response_object, 200
#     else:
#     	response_object = {
#     	'status' = 'failed',
#     	'message' = 'failed'
#     	}




def delete_evacuees(home_id):
	evacuees = Evacuees.query.filter_by(home_id=home_id).first()
	if evacuees:
			db.session.delete(evacuees)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'evacuee has been deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'evacuee does not exist'
		}
		return response_object, 409
		
def search_by_name(search_term):
	results = Evacuees.query.filter(Evacuees.name.match('%'+search_term+'%')).all()
	return results

def search_by_address(search_term):
	results = Evacuees.query.filter(Evacuees.address.match('%'+search_term+'%')).all()
	return results

def search_by_home_id(search_term):
	results = Evacuees.query.filter(Evacuees.home_id.match('%'+search_term+'%')).all()
	return results