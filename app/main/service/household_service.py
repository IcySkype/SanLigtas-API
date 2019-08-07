import uuid
import datetime

from app.main import db
from app.main.model.household import House


def save_new_house(data):
    household = House.query.filter_by(address=data['address']).first()
    if not household:
        new_house = House(
            public_id=str(uuid.uuid4()),
            address=data['address']
		)
        save_changes(new_house)
        response_object = {
            'status' : 'success',
            'message' : 'Household added'
        }
        return response_object, 201
    else:
        response_object = {
			'status' : 'fail',
			'message' : 'Address already used.'
		}
        return response_object, 409

def get_all_houses():
	return House.query.all()


def get_a_house(public_id):
	return House.query.filter_by(public_id=public_id).first()

def delete_house(public_id):
	db.session.delete(public_id)
	db.session.commit()

#THERE IS NO UPDATE HOUSEHOLD, since nothing needs to be edited/updated.

def save_changes(data):
	db.session.add(data)
	db.session.commit()
