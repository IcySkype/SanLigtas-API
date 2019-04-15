import uuid
import datetime

from app.main import db
from app.main.model.user import UserMobile


def save_new_user(data):
	user = UserMobile.query.filter_by(email=data['email']).first()
	if not user:
		new_user = UserMobile(
			public_id=str(uuid.uuid4()),
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_date=data['birth_date'],
            address=data['address'],
            contact_number=data['contact_number'],
            gender=data['gender'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
		)
		save_changes(new_user)
		return generate_token(new_user)
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Email already used.'
		}
		return response_object, 409


def get_all_users():
	return UserMobile.query.all()


def get_a_user(public_id):
	return UserMobile.query.filter_by(public_id=public_id).first()

def delete_user(public_id):
	db.session.delete(public_id)
	db.session.commit()

def update_user(public_id, data):
    user = UserMobile.query.filter_by(public_id=public_id).first()
    if user:
        user.public_id = str(uuid.uuid4()),
        user.email = data['email']
        user.username = data['username']
        user.password = data['password']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.birth_date = data['birth_date']
        user.address = data['address']
        user.contact_number = data['contact_number']
        user.gender = data['gender']

        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'Updated User.'
        }
        return response_object, 200
        if UserMobile.query.filter_by(email=data['email']).count() == 0 or User.query.filter_by(email=data['email']).count() == 1 and user.email == newdata['email']:
            user.public_name = str(uuid.uuid4()),
            user.email = data['email'],
            user.birth_date = data['birth_date'],
            user.contact_number = data['contact_number'],
            user.address = data['address']
            user.username = data['username'],
            user.first_name = data['first_name'],
            user.last_name = data['last_name'],
            user.password = data['password'],
            user.gender = data['gender']
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'user updated'
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'failed',
                'message': 'email already used.'
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'Failed',
            'message': 'No user found',
            'status': 'failed',
            'message': 'no user found.'
        }
        return response_object, 409


def save_changes(data):
	db.session.add(data)
	db.session.commit()

def generate_token(user):
	try:
		auth_token = user.encode_auth_token(user.id)
		response_object = {
			'status' : 'success',
			'message' : 'Successfully registered',
			'Authorization' : auth_token.decode()
		}
		return response_object, 201
	except Exception as e:
		response_object = {
			'status' : 'fail',
			'message' : 'Some error occurred. Please try again.'
			}
		return response_object, 401