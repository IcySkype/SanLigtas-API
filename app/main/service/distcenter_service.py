from sqlalchemy import and_
import uuid
import datetime
import requests, json

from app.main import db
from app.main.model.distcenter import DistCenter, AssignedCenter



def assign_admin(data):
	print(data)
	print(data["center_admin"])

	admin = AssignedCenter.query.filter((AssignedCenter.center_admin == data["center_admin"]) & (AssignedCenter.center_public_id == data["center_public_id"])).first()
	if not admin:
		new_admin = AssignedCenter(
			center_public_id=data["center_public_id"],
			center_admin=data["center_admin"]
			)
		save_changes(new_admin)
		print('mao ni siya dzaii')
		response_object = {
			'status': 'success',
			'message': 'admin assigned successfully'
		}
		return response_object, 201
	else:
		response_object = {
			'status': 'fail',
			'message': 'Admin already assigned'
		}
		return response_object, 409


def save_new_dcenter(data):
	dcenter = DistCenter.query.filter_by(address=data['address']).first()
	if not dcenter:
		addr = data['address']

		google_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+addr+'&key=AIzaSyAayoLLtuuXjGtgaxIURWpfzRrGDZ1KgVc')
		google_dict = json.loads(google_response.text)
		print(google_dict)
		latitude=google_dict['results'][0]['geometry']['location']['lat']
		longitude=google_dict['results'][0]['geometry']['location']['lng']



		new_dcenter = DistCenter(
			name=data['name'],
			address=data['address'],
			capacity=data['capacity'],
			latitude=latitude,
			longitude=longitude,
			public_id=str(uuid.uuid4())
		)
		save_changes(new_dcenter)
		response_object = {
			'status' : 'success',
			'message' : 'distribution center added'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Name already used.'
		}
		print(response_object)
		return response_object, 409


def get_all_dcenters():
	return DistCenter.query.all()

def get_a_dcenter(public_id):
	return DistCenter.query.filter_by(public_id=public_id).first()


def save_changes(data):
	db.session.add(data)
	db.session.commit()



def update_dcenter(public_id, data):
	dcenter = DistCenter.query.filter_by(public_id=public_id).first()
	otherdcenters = DistCenter.query.filter(DistCenter.public_id != public_id).all()
	if dcenter:
		check_existing = True
		for x in otherdcenters:
			if x.id == data['address']:
				check_existing = False
		if check_existing:
			dcenter.name=data['name'],
			dcenter.address=data['address'],
			dcenter.capacity=data['capacity']
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'distribution center updated'
			}
			return response_object, 200
		else:
			print(data['address'])
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


def delete_dcenter(public_id):
	dcenter = DistCenter.query.filter_by(public_id=public_id).first()
	if dcenter:
			db.session.delete(dcenter)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'distribution center deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching distribution center found.'
		}
		return response_object, 409
		


def search_center(search_term):
	results = DistCenter.query.filter(((DistCenter.name.like("%"+search_term+"%")) | (DistCenter.address.like("%"+search_term+"%")) | (DistCenter.public_id.like("%"+search_term+"%")))).all()
	print(results)
	return results


def get_assigned_admin(center_public_id):

	admin = AssignedCenter.query.filter_by(center_public_id=center_public_id).all()

	return admin