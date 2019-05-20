import datetime
import uuid

from app.main import db
from app.main.model.dependents import Dependents
from app.main.model.evacuees import Evacuees


def save_new_dependents(data):
	dependents = Dependents.query.filter((Dependents.home_id == data["home_id"]) & (Dependents.name == data["name"])).first()
	if not dependents:
		print(data)
		

		new_dependents = Dependents(
			name=data['name'],
			dependents_id=str(uuid.uuid4()),
			home_id = data['home_id'],
			address=data['address'],
			gender=data['gender'],
			age=data['age'],
			educ_attainment=data['educ_attainment'],
			occupation=data['occupation']
		)
		save_changes(new_dependents)
		response_object = {
			'status' : 'success',
			'message' : 'dependents added'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'dependents id has been already used'
		}
		return response_object, 409


def get_all_dependents():
	return Dependents.query.all()


def get_a_dependent(dependents_id):
	return Dependents.query.filter_by(dependents_id=dependents_id).first()

def delete_dependents(dependents_id):
	dependents = Dependents.query.filter_by(dependents_id=dependents_id).first()
	if dependents:
		db.session.delete(dependents)
		db.session.commit()
		response_object = {
			'status' : 'success',
			'message' : 'dependents deleted'
		}
		return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching dependents found.'
		}
		return response_object, 409


def update_dependent(dependents_id, data):
    # user = UserAdmin.query.filter_by(public_id=public_id).first()
    dependent = db.session.query(Dependents).filter_by(dependents_id=dependents_id).first()
    if dependent:
        dependent.address = data['address']
        dependent.name = data['name']
        dependent.gender = data['gender']
        dependent.age = data['age']
        dependent.educ_attainment = data['educ_attainment']
        dependent.occupation = data['occupation']

        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'Updated Dependent.'
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


def delete_dependents(dependents_id):
	dependents = Dependents.query.filter_by(dependents_id=dependents_id).first()
	if dependents:
			db.session.delete(dependents)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'dependents has been deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'dependents does not exist'
		}
		return response_object, 409



def search_dependent(search_term):
	print(search_term)
	results = Dependents.query.filter(((Dependents.name.like("%"+search_term+"%")) | (Dependents.address.like("%"+search_term+"%")) | (Dependents.gender.like("%"+search_term+"%")) | (Dependents.dependents_id.like("%"+search_term+"%")))).all()
	return results


	