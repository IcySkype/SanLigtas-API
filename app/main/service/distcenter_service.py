import uuid
import datetime

from app.main import db
from app.main.model.distcenter import DistCenter, Barangay
from app.main.model.user import Account
from app.main.model.evacuees import Evacuees

#initializes barangay table with default barangays.
def brgy_init():
	if Barangay.query.count() == 0:
		default_brgy = ['Tambo', 'Hinaplanon', 'San Roque']
		for name in default_brgy:
			new_brgy = Barangay(name=name)
			db.session.add(new_brgy)
			db.session.commit()
			
def check_brgy(id):
	brgy = Barangay.query.filter_by(id=id).first()
	return brgy.name

def save_new_dcenter(data):
	dcenter = DistCenter.query.filter_by(name=data['name']).first()
	if not dcenter:
		new_dcenter = DistCenter(
			name=data['name'],
			barangay_id=data['barangay'],
			capacity=data['capacity'],
			public_id=str(uuid.uuid4())
		)
		save_changes(new_dcenter)
		response_object = {
			'status' : 'Success.',
			'message' : 'Center added.'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Name already used.'
		}
		return response_object, 409

def get_all_dcenters():
	return DistCenter.query.all()

def get_a_dcenter(public_id):
	return DistCenter.query.filter_by(public_id=public_id).first()

def get_all_sorted():
	return db.session.query(DistCenter.public_id, DistCenter.name, Barangay.name, DistCenter.capacity).outerjoin(Barangay, DistCenter.public_id == Barangay.id).all()

def save_changes(data):
	db.session.add(data)
	db.session.commit()

def update_dcenter(public_id, data):
	dcenter = DistCenter.query.filter_by(public_id=public_id).first()
	otherdcenters = DistCenter.query.filter(DistCenter.public_id != public_id).all()
	if dcenter:
		name_exists = False
		for x in otherdcenters:
			if x.name == data['name']:
				name_exists = True
		if not name_exists:
			dcenter.name=data['name'],
			dcenter.barangay_id=data['barangay'],
			dcenter.capacity=data['capacity']
			db.session.commit()
			response_object = {
			'status' : 'Success',
			'message' : 'Center updated.'
			}
			return response_object, 200
		else:
			response_object = {
			'status' : 'fail',
			'message' : 'New Name already exists'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching Center found.'
		}
		return response_object, 409

def delete_dcenter(public_id):
	dcenter = DistCenter.query.filter_by(public_id=public_id).first()
	if dcenter:
			db.session.delete(dcenter)
			db.session.commit()
			response_object = {
			'status' : 'Success',
			'message' : 'Center deleted.'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching Center found.'
		}
		return response_object, 409
		
def search_center(search_term):
	return DistCenter.query.filter(DistCenter.name.like("%"+search_term+"%")).all()

def manage(public_id, user_id):
	center = DistCenter.query.filter_by(public_id=public_id).first()
	admin = Account.query.filter_by(public_id=user_id).first()
	if center and admin:
		if admin.role_id != 1:
			admin.centers.append(center)
			db.session.commit()
			response_object = {
			'status' : 'Success',
			'message' : 'Manager added.'
			}
			return response_object, 200
		else:
			response_object = {
			'status' : 'Fail',
			'message' : 'Manager cannot be Normal User'
			}
			return response_object, 409
	else:
		response_object = {
			'status' : 'Fail',
			'message' : 'No such user or center exists.'
		}
		return response_object, 409
		
def register(public_id, evac_id):
	center = DistCenter.query.filter_by(public_id=public_id).first()
	evacuee = Evacuees.query.filter_by(public_id=evac_id).first()
	if center and evacuee:
		center.evacs.append(evacuee)
		db.session.commit()
		response_object = {
			'status' : 'Success',
			'message' : 'Evacuee registered to center.'
		}
		return response_object, 200
	else:
		response_object = {
			'status' : 'Fail',
			'message' : 'No such evacuee or center exists.'
		}
		return response_object, 409