from .. import db
from app.main.model.distcenter import Barangay


class Evacuees(db.Model):
	__tablename__ = "evacuees"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	public_id = db.Column(db.String(300), nullable = False, unique=True)

	first_name = db.Column(db.String(50), nullable = False)
	middle_name = db.Column(db.String(50), nullable = False)
	last_name = db.Column(db.String(50), nullable = False)
	
	age = db.Column(db.Integer(), nullable = True)
	gender = db.Column(db.String(300), nullable = True)
	religion = db.Column(db.String(300), nullable = True)
	civil_status = db.Column(db.String(300), nullable = True)
	date_of_reg = db.Column(db.DateTime(), nullable = True)
	
	family_id = db.Column(db.String(300), db.ForeignKey('family.public_id'), nullable=True)
	barangay_id = db.Column(db.Integer(), db.ForeignKey('barangay.id'))
	center_id = db.Column(db.String(300), db.ForeignKey('distcenter.public_id'), nullable=True)
	
class Family(db.Model):
	__tablename__ = "family"
	
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False, unique=True)
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	members = db.relationship('Evacuees', backref='family')


