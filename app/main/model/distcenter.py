from .. import db


class DistCenter(db.Model):
	__tablename__ = "distcenter"
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), unique=True, nullable = False)
	barangay_id = db.Column(db.Integer(), db.ForeignKey('barangay.id'))
	capacity = db.Column(db.Integer(), nullable = False)
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	
class Barangay(db.Model):
	__tablename__ = "barangay"
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	center = db.relationship('DistCenter', backref='barangay')
	evacuees = db.relationship('Evacuees', backref='barangay')