import uuid
import datetime

from app.main import db
from app.main.model.goods import Goods, GoodType
from app.main.model.distcenter import DistCenter

def type_init():
	if GoodType.query.count() == 0:
		default_type= ['Money', 'Food', 'Clothing', 'Cleaning', 'Misc']
		for name in default_type:
			new_brgy = GoodType(name=name)
			db.session.add(new_brgy)
			db.session.commit()
			
def check_type(id):
	brgy = GoodType.query.filter_by(id=id).first()
	return brgy.name

def save_new_rgoods(data):
	rgoods = Goods.query.filter_by(name=data['name'], center_id=data['center_id']).first()
	if not rgoods:
		dcenter = DistCenter.query.filter_by(public_id=data['center_id']).first()
		if not dcenter:
			response_object = {
				'status' : 'fail',
				'message' : 'Center does not exist.'
			}
			return response_object, 409
		new_goods = Goods(
			name=data['name'],
			details=data['details'],
			type=data['type'],
			amount=data['amount'],
			received_date=datetime.datetime.utcnow(),
			distribution_date=None,
			status="New",
			isActive=True,
			public_id=str(uuid.uuid4()),
			center_id=data['center_id']
		)
		save_changes(new_goods)
		response_object = {
			'status' : 'success',
			'message' : 'Relief Goods added.'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Goods already exist for that center. Try restocking.'
		}
		return response_object, 409


def get_all_rgoods():
	return Goods.query.all()

def get_rgoods(public_id):
	return Goods.query.filter_by(public_id=public_id).first()

def save_changes(data):
	db.session.add(data)
	db.session.commit()

def update_rgoods(public_id, data):
	#public_id should not change.
	rgoods = Goods.query.filter_by(public_id=public_id).first()
	if rgoods:
		name=data['name']
		details=data['details']
		type=data['type']
		amount=data['amount']
		received_date=datetime.datetime.utcnow()
		status=data['status']
		isActive=True
		db.session.commit()
		response_object = {
			'status' : 'success',
			'message' : 'Goods updated'
		}
		return response_object, 200
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching goods found.'
		}
		return response_object, 409

def distribute(public_id):
	rgoods = Goods.query.filter_by(public_id=public_id).first()
	if rgoods:
		rgoods.distribution_date=datetime.datetime.utcnow(),
		rgoods.status="Distributed"
		db.session.commit()
		response_object = {
			'status' : 'success',
			'message' : 'Goods distributed'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching goods found.'
		}
		return response_object, 409


def delete_rgoods(public_id):
	rgoods = Goods.query.filter_by(public_id=public_id).first()
	if rgoods:
			rgoods.isActive = False
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'Goods deactivated'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching goods found.'
		}
		return response_object, 409
