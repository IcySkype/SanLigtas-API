import uuid
import datetime

from app.main import db
from app.main.model.user import User, Account, Role

#initializes user role table with default roles.
def role_init():
	if Role.query.count() == 0:
		default_roles = ['Normal', 'Social Worker', 'Admin']
		for role in default_roles:
			new_role = Role(name=role)
			db.session.add(new_role)
			db.session.commit()
			
def check_role(role_id):
	role = Role.query.filter_by(id=role_id).first()
	return role.name
		
#account details saved to account table. user details saved to user table.
def save_new_user(data):
	user = Account.query.filter_by(username=data['username']).first()
	if not user:
		id=str(uuid.uuid4())
		new_acc = Account(
			public_id = id,
			username=data['username'],
			password=data['password'],
			role_id=data['role_id'],
			isActive=True
			)
		new_user = User(
			acc_id=id,
			first_name=data['first_name'],
			middle_name=data['middle_name'],
			last_name=data['last_name'],
			gender=data['gender'],
			registered_on=datetime.datetime.utcnow()
		)
		save_changes(new_acc, new_user)
		return generate_token(new_acc)
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Email already used.'
		}
		return response_object, 409

#checks if old password matches. then changes pass to new password
def update_password(username, data):
	user = Account.query.filter_by(username=username).first()
	if user and user.check_password(data.get('old_pass')):
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


#account left outer join user
def get_all_users():
	return db.session.query(Account.public_id, Account.username, User.first_name, User.middle_name, User.last_name, User.gender, User.registered_on, Account.role, Account.isActive).outerjoin(User, Account.public_id == User.acc_id).all()

#account left outer join user, specific user
def get_a_user(public_id):
	return db.session.query(Account.public_id, Account.username, User.first_name, User.middle_name, User.last_name, User.gender, User.registered_on, Account.role, Account.isActive).outerjoin(User, Account, Account.public_id == User.acc_id).filter(Account.public_id == public_id)


#delete is now deactivate.
def delete_user(public_id):
	user = Account.query.filter_by(public_id=public_id).first()
	user.isActive = False
	db.session.commit()
	response_object = {
		'status': 'Success',
		'message': 'Delete Successful.'
	}
	return response_object, 200

#can't update username
def update_user(public_id, data):
	user = User.query.filter_by(acc_id=public_id).first()
	if user:
		user.first_name=data['first_name']
		user.middle_name=data['middle_name']
		user.last_name=data['last_name']
		user.gender=data['gender']
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

#search using username
def search_by_user(search_term):
	results = Account.query.filter(Account.username.like("%"+search_term+"%")).all()
	return results


def save_changes(data1, data2):
	db.session.add(data1)
	db.session.add(data2)
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