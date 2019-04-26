import datetime

from app.main import db
from app.main.model.dependents import Dependents


def save_new_dependents(data):
	dependents = Dependents.query.filter_by(dependents_id=data['dependents_id']).first()
	if not dependents:
		new_dependents = Dependents(
			name=data['name'],
			home_id=data['home_id'],
			dependents_id=data['dependents_id'],
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


def get_a_dependents(dependents_id):
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

def update_dependents(dependents_id, data):
	dependents = Dependents.query.filter_by(dependents=dependents).first()
	otherDependets = Dependents.query.filter(Dependents.dependents_id != dependents_id).all()
	if dependents:
		check_existing = False
		for x in otherDependets:
			if x.id == data['address']:
				check_existing = True
		if check_existing:
			evacuees.name = data['name']
			evacuees.address = data['address'],
			evacuees.dependents_id = data['dependents_id'],
			evacuees.gender = data['gender'],
			evacuees.age = data['age'],
			evacuees.educ_attainment = data['educ_attainment'],
			evacuees.occupation = data['occupation']
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'dependents updated'
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
			'message' : 'No matching dependents found.'
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