import uuid
import datetime

from app.main import db
from app.main.model.evacuees import Evacuees
from app.main.model.household import House

def save_new_evacuees(data):
	household = House.query.filter_by(public_id=data['home_id']).first()
	house_members = Evacuees.query.filter_by(home_id=data['home_id']).all()
	if household:
		check_existing = False
		has_leader = False
		for x in house_members:
			if x.name == data['name']:
				check_existing = True
			if x.is_house_leader:
				has_leader = True
		if not check_existing:
			if has_leader and data['is_house_leader']=='true':
				response_object = {
				'status' : 'failed',
				'message' : 'Household already has leader. Error in adding evacuee as household leader.'
				}
				return response_object, 409

			new_evacuees = Evacuees(
				name=data['name'],
				home_id=data['home_id'],
				is_house_leader=int(data['is_house_leader'] == 'true'),
				public_id=str(uuid.uuid4()),
				date_of_reg=datetime.datetime.utcnow(),
				gender=data['gender'],
				age=data['age'],
				religion=data['religion'],
				civil_status=data['civil_status'],
				educ_attainment=data['educ_attainment'],
				occupation=data['occupation']
			)
			save_changes(new_evacuees)
			response_object = {
				'status' : 'success',
				'message' : 'Evacuee added'
			}
			return response_object, 201
		else:
			response_object = {
				'status' : 'failed',
				'message' : 'Evacuee name already exists in household'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Household does not exist'
		}
		return response_object, 409


def get_all_evacuees():
	return Evacuees.query.all()

def get_evacuees_by_house(home_id):
	return Evacuees.query.filter_by(home_id=home_id).all()

def get_an_evacuee(public_id):
	return Evacuees.query.filter_by(public_id=public_id).first()

def delete_evacuees(public_id):
	evacuees = Evacuees.query.filter_by(public_id=public_id).first()
	if evacuees:
			db.session.delete(evacuees)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'Evacuee deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching evacuees found.'
		}
		return response_object, 409

def update_evacuees(public_id, data):
	#cannot update: home_id, is_house_leader, public_id
	evacuee = Evacuees.query.filter_by(public_id=public_id).first()
	if evacuee:
		household = House.query.filter_by(public_id=evacuee.home_id).first()
		house_members = Evacuees.query.filter(Evacuees.public_id != public_id, Evacuees.home_id==evacuee.home_id).all()
		if household:
			check_existing = False
			for x in house_members:
				if x.name == data['name']:
					check_existing = True

			if not check_existing:
				evacuee.name = data['name']
				evacuee.gender = data['gender']
				evacuee.age = data['age']
				evacuee.religion = data['religion']
				evacuee.civil_status = data['civil_status']
				evacuee.educ_attainment = data['educ_attainment']
				evacuee.occupation = data['occupation']
				db.session.commit()
				response_object = {
				'status' : 'success',
				'message' : 'Evacuees updated'
				}
				return response_object, 200
			else:
				response_object = {
				'status' : 'fail',
				'message' : 'Name chosen for replacement has already been taken'
				}
				return response_object, 409
		else:
			response_object = {
				'status' : 'fail',
				'message' : 'Household not found.'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching evacuee found.'
		}
		return response_object, 409

def save_changes(data):
	db.session.add(data)
	db.session.commit()
		
def search_by_name(search_term):
	results = Evacuees.query.filter(Evacuees.name.ilike('%'+search_term+'%')).all()
	return results

def statistics_age():
	data = {'list': []}
	for x in range(125):
		if statistics_by_age(x) != None:
			data['list'].append(statistics_by_age(x))
	return data


def statistics_by_age(age):
	counter = Evacuees.query.filter_by(age=age).count()
	if counter > 0:
		return { 'age' : age, 'count' : counter }
	else:
		return None