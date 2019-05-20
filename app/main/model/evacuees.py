from .. import db
from app.main.model.dependents import Dependents
from app.main.model.distcenter import DistCenter


class Evacuees(db.Model):
	__tablename__ = "evacuees"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	home_id = db.Column(db.Integer(), unique = True)
	name = db.Column(db.String(50), nullable = False)
	address = db.Column(db.String(300), nullable = False)
	date_of_reg = db.Column(db.DateTime(), nullable = False)
	gender = db.Column(db.String(300), nullable = False)
	age = db.Column(db.Integer(), nullable = False)
	religion = db.Column(db.String(300), nullable = False)
	civil_status = db.Column(db.String(300), nullable = False)
	educ_attainment = db.Column(db.String(300), nullable = False)
	occupation = db.Column(db.String(300), nullable = False)
	center_id = db.Column(db.Integer(), db.ForeignKey('distcenter.id'))
	dependent = db.relationship('Dependents', backref='dependents_homeID')
	# center = db.relationship('AssignedCenter', backref='center', lazy='dbynamic', primaryjoin="DistCenter.id == Evacuees.center_id")


