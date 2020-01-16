from .. import db

class Announcement(db.Model):
	__tablename__ = "announcement"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	title = db.Column(db.String(50), nullable = False)
	details = db.Column(db.String(300), nullable=True)
	post_date = db.Column(db.DateTime(), nullable=False)
	last_edit_date = db.Column(db.DateTime(), nullable=False)
	isActive = db.Column(db.Boolean(), nullable=False)
	type = db.Column(db.Integer(), db.ForeignKey('announce_type.id'))
	
class AnnounceType(db.Model):
	__tablename__ = "announce_type"
	
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	announcements = db.relationship('Announcement', backref='announcement_type')