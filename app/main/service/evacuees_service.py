import uuid
import datetime

from app.main import db
from app.main.model.evacuees import Evacuees, Family
from app.main.model.distcenter import DistCenter

#Evacuee Family Services
def get_family(public_id):
	return Family.query.filter_by(public_id=public_id).first()
	#to get specific family member, use FamilyObject.members[0-...]
	
def get_all_families():
	return Family.query.all()

def create_family(data):
	family = Family.query.filter_by(name=data['name']).all()
	if not family:
		new_family = Family(
			name = data['name'],
			public_id=str(uuid.uuid4())
		)
		save_changes(new_family)
		response_object = {
			'status' : 'Success',
			'message' : 'Family created.'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'Failed',
			'message' : 'Family exists.'
		}
		return response_object, 409
		
def edit_family(public_id, data):
	family = Family.query.filter_by(public_id=public_id).first()
	if family:
		if Family.query.filter_by(name=data['name']).count() == 0:
			family.name = data['name']
			db.session.commit()
			save_changes(new_family)
			response_object = {
				'status' : 'Success',
				'message' : 'Family name changed.'
			}
			return response_object, 201
		else:
			response_object = {
				'status' : 'Failed',
				'message' : 'Family name already exists.'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'Failed',
			'message' : 'Family exists.'
		}
		return response_object, 409
		
def delete_family(public_id):
	family = Family.query.filter_by(public_id=public_id).first()
	if family:
		db.session.delete(family)
		db.session.commit()
		response_object = {
			'status' : 'success',
		'message' : 'Family removed.'
		}
		return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching family found.'
		}
		return response_object, 409
		
#Evacuee Services
def save_new_evacuees(data):
	evacuee = Evacuees.query.filter_by(first_name=data['first_name'], middle_name=data['middle_name'], last_name=data['last_name']).all()
	if not evacuee:
		new_evacuees = Evacuees(
			public_id=str(uuid.uuid4()),
			
			first_name=data['first_name'],
			middle_name=data['middle_name'],
			last_name=data['last_name'],

			age=data['age'],
			gender=data['gender'],
			religion=data['religion'],
			civil_status=data['civil_status'],
			date_of_reg=datetime.datetime.utcnow(),
			
			family_id=data['family'], #Evacuee can have NULL family.
			barangay_id=data['barangay']
		)
		save_changes(new_evacuees)
		response_object = {
			'status' : 'success',
			'message' : 'Evacuee added'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Evacuee does not exist.'
		}
		return response_object, 409


def get_all_evacuees():
	return Evacuees.query.all()

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
	evacuee = Evacuees.query.filter_by(public_id=public_id).first()
	if evacuee:
		#if no other evacuee shares new name, then update
		if Evacuees.query.filter_by(first_name=data['first_name'], middle_name=data['middle_name'], last_name=data['last_name']).count == 0:
			evacuee.first_name=data['first_name']
			evacuee.middle_name=data['middle_name']
			evacuee.last_name=data['last_name']

			evacuee.age=data['age']
			evacuee.gender=data['gender']
			evacuee.religion=data['religion']
			evacuee.civil_status=data['civil_status']

			evacuee.family_id=data['family'] #Evacuee can have NULL family.
			evacuee.barangay_id=data['barangay']
			
			db.session.commit()
			response_object = {
				'status' : 'Success',
				'message' : 'Evacuee updated.'
			}
			return response_object, 200
		else:
			response_object = {
				'status' : 'Fail',
				'message' : 'There already exists someone with that name.'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'Fail',
			'message' : 'Evacuee not found.'
		}
		return response_object, 409

def save_changes(data):
	db.session.add(data)
	db.session.commit()
		
def search_by_name(search_term):
	results = Evacuees.query.filter((Evacuees.first_name.ilike('%'+search_term+'%'))|(Evacuees.middle_name.ilike('%'+search_term+'%')) | (Evacuees.last_name.ilike('%'+search_term+'%'))).all()
	return results
	
def search_family(search_term):
	results = Family.query.filter(Family.name.ilike('%'+search_term+'%')).all()
	return results

def stat_AgeVsGender(gender):
	#Warning: 'Male' != 'male'. will display different numbers.
	data = {'list': []}
	#age group: Baby/Toddler, Child, Adolescent, Adult, Senior
	age_group = ['0-3', '4-10','10-19', '20-50', '51-150']
	switcher = {
		'0-3': (0,3),
		'4-10': (4,10),
		'10-19': (10,19),
		'20-50': (20,50),
		'51-150': (51,150)
	}
	for x in age_group:	
		min = switcher[x][0]
		max = switcher[x][1]
		total = 0
		for y in range(min,max):
			counter = Evacuees.query.filter_by(age=y, gender=gender).count()
			total = total + counter
		data['list'].append({ x: total })
	return data


