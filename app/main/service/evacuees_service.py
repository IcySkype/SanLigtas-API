import datetime

from app.main import db
from app.main.model.evacuees import Evacuees




def add_evacuee(data):
	print(data)
	evacuee = Evacuees.query.filter((Evacuees.home_id == data["home_id"]) & (Evacuees.center_id == data["center_id"])).first()

	if not evacuee:
		evacuee = Evacuees.query.filter_by(home_id=data["home_id"]).first()

		evacuee.center_id=data["center_id"]

		db.session.commit()

		response_object = {
			'status': 'success',
			'message': 'Evacuee successfully assigned'
		}
		return response_object, 200
	else:
		response_object = {
			'status': 'fail',
			'message': 'Evacuee already assigned.'
		}
		return response_object, 409



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
	evac = Evacuees.query.filter_by(home_id=home_id).first()
	if dcenter:
			db.session.delete(evac)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'Evacuee deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching evacuee found.'
		}
		return response_object, 409
		


def update_evacuees(home_id, data):
    evacuee = db.session.query(Evacuees).filter_by(home_id=home_id).first()
    if evacuee:
        evacuee.name = data['name']
        evacuee.address = data['address']
        evacuee.gender = data['gender']
        evacuee.age = data['age']
        evacuee.religion = data['religion']
        evacuee.civil_status = data['civil_status']
        evacuee.educ_attainment = data['educ_attainment']
        evacuee.occupation = data['occupation']

        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'Updated Evacuee.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'Failed',
            'message': 'No user found'
        }
        return response_object, 409




def save_changes(data):
	db.session.add(data)
	db.session.commit()



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



def search_evacuee(search_term):
	print(search_term)
	results = Evacuees.query.filter(((Evacuees.name.like("%"+search_term+"%")) | (Evacuees.address.like("%"+search_term+"%")) | (Evacuees.gender.like("%"+search_term+"%")))).all()
	return results


	