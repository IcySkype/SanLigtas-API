import uuid
import datetime

from app.main import db
from app.main.model.user import UserAdmin


def save_new_user(data):
    print(data)
    user = UserAdmin.query.filter_by(email=data['email']).first()
    if not user:
        new_user = UserAdmin(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            role=data['role'],
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


def update_password(public_id, data):
    user = UserAdmin.query.filter_by(public_id=public_id).first()
    if user:
        user.password = data['new_pass']
        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'Password successfully updated.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'Failed',
            'message': 'Password cannot change'
        }
        return response_object, 409


def get_all_users():
	return UserAdmin.query.all()


def get_a_user(public_id):
	return UserAdmin.query.filter_by(public_id=public_id).first()

def delete_user(public_id):
	db.session.delete(public_id)
	db.session.commit()

def update_user(public_id, data):
    # user = UserAdmin.query.filter_by(public_id=public_id).first()
    user = db.session.query(UserAdmin).filter_by(public_id=public_id).first()
    if user:
        user.username = data['username']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.role = data['role']
        user.gender = data['gender']

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



def search_by_user(search_term):
    results = UserAdmin.query.filter(((UserAdmin.username.like("%"+search_term+"%")) | (UserAdmin.gender.like("%"+search_term+"%")) | (UserAdmin.role.like("%"+search_term+"%")) | (UserAdmin.public_id.like("%"+search_term+"%")) | (UserAdmin.first_name.like("%"+search_term+"%")) | (UserAdmin.last_name.like("%"+search_term+"%")))).all()
    return results



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