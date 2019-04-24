import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
	user = User.query.filter_by(email=data['email']).first()
	if not user:
		new_user = User(
			public_id=str(uuid.uuid4()),
			email=data['email'],
			username=data['username'],
			password=data['password'],
			role=data['role'],
			first_name=data['first_name'],
			last_name=data['last_name'],
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
	return User.query.all()


def get_a_user(public_id):
	return User.query.filter_by(public_id=public_id).first()

def delete_user(user):
	db.session.delete(user)
	db.session.commit()

def update_user(public_id, data):
    user = User.query.filter_by(public_id=public_id).first()
    if user:
        user.email = data['email']
        user.username = data['username']
        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'Updated User.'
        }
        return response_object, 200
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