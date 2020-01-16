import uuid
import datetime

from app.main import db
from app.main.model.announcements import Announcement, AnnounceType

#initializes announcement types
def type_init():
	if AnnounceType.query.count() == 0:
		default_types = ['Important', 'Reminder', 'Notice']
		for type in default_types:
			new_type = AnnounceType(name=type)
			db.session.add(new_type)
			db.session.commit()
		
#account details saved to account table. user details saved to user table.
def create_announcement(data):
	new_ann = Announcement(
		public_id = str(uuid.uuid4()),
		title=data['title'],
		details=data['details'],
		post_date=datetime.datetime.utcnow(),
		last_edit_date=datetime.datetime.utcnow(),
		isActive=True,
		type=data['type']
	)
	save_changes(new_ann)
	response_object = {
		'status' : 'Success',
		'message' : 'Announcement posted.'
	}
	return response_object, 201

def get_announcement_board():
	return Announcement.query.all()

def get_announcement(public_id):
	return Announcement.query.filter_by(public_id=public_id)


def deactivate_announcement(public_id):
	ann = Announcement.query.filter_by(public_id=public_id).first()
	ann.isActive = False
	db.session.commit()
	response_object = {
		'status': 'Success',
		'message': 'Delete Successful.'
	}
	return response_object, 200

def update_announcement(public_id, data):
	ann = Announcement.query.filter_by(public_id=public_id).first()
	if ann:
		ann.title=data['title']
		ann.details=data['details']
		ann.last_edit_date=datetime.datetime.utcnow()
		ann.type=data['type']
		db.session.commit()
		response_object = {
			'status': 'Success',
			'message': 'Updated Announcement.'
		}
		return response_object, 200
	else:
		response_object = {
			'status': 'Failed',
			'message': 'No such announcement posted'
		}
		return response_object, 409

def save_changes(data):
	db.session.add(data)
	db.session.commit()