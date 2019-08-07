import uuid
import datetime

from app.main import db
from app.main.model.goods import RGoods
from app.main.model.distcenter import DistCenter


def save_new_rgoods(data):
	rgoods = RGoods.query.filter_by(code=data['code']).first()
	dcenter = DistCenter.query.filter_by(public_id=data['center_id']).first()
	if not dcenter:
		response_object = {
			'status' : 'fail',
			'message' : 'Distribution Center does not exist.'
		}
		return response_object, 409
	if not rgoods:
		new_goods = RGoods(
			name=data['name'],
			code=data['code'],
			type=data['type'],
			amount=data['amount'],

			center_id=data['center_id'],
			received_date=data['received_date'],
			received_from=data['received_from'],
			#distribution_date=data['distribution_date'],

			expiry=data['expiry'],
			size=data['size'],
			clothing_type=data['clothing_type'],
			condition=data['condition'],

			status="New"
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
			'message' : 'Code already used.'
		}
		return response_object, 409


def get_all_rgoods():
	return RGoods.query.all()

def get_rgoods(code):
	return RGoods.query.filter_by(code=code).first()

def save_changes(data):
	db.session.add(data)
	db.session.commit()

def update_rgoods(code, data):
	#code should not change.
	rgoods = RGoods.query.filter_by(code=code).first()
	dcenter = DistCenter.query.filter_by(public_id=data['center_id']).first()
	if not dcenter:
		response_object = {
			'status' : 'fail',
			'message' : 'Distribution Center does not exist.'
		}
		return response_object, 409
	if rgoods:
		rgoods.name=data['name'],
		rgoods.code=data['code'],
		rgoods.type=data['type'],
		rgoods.amount=data['amount'],

		rgoods.center_id=data['center_id'],
		rgoods.received_date=data['received_date'],
		rgoods.received_from=data['received_from'],
		rgoods.distribution_date=data['distribution_date'],

		rgoods.expiry=data['expiry'],
		rgoods.size=data['size'],
		rgoods.clothing_type=data['clothing_type'],
		rgoods.condition=data['condition'],

		rgoods.status=data['status']

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

def distribute(code, date):
	rgoods = RGoods.query.filter_by(code=code).first()
	if rgoods:
		rgoods.distribution_date=date,
		rgoods.status="Distributed"
		db.session.commit()
		response_object = {
			'status' : 'success',
			'message' : 'Goods distributed'
		}
		return response_object, 200
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching goods found.'
		}
		return response_object, 409


def delete_rgoods(code):
	rgoods = RGoods.query.filter_by(code=code).first()
	if rgoods:
			db.session.delete(rgoods)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'Goods deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching goods found.'
		}
		return response_object, 409
		

def search_center(search_term):
	results = RGoods.query.filter(RGoods.center_id.like("%"+search_term+"%"))
	print(results)
	return results

def search_code(search_term):
	results = RGoods.query.filter(RGoods.code.like("%"+search_term+"%"))
	print(results)
	return results
