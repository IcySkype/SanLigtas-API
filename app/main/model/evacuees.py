from .. import db
from app.main.model.household import House


class Evacuees(db.Model):
	__tablename__ = "evacuees"
	#Identifications
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	home_id = db.Column(db.String(100), db.ForeignKey('household.public_id'), nullable=True)
	is_house_leader = db.Column(db.Boolean())
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	#important personal identifiers
	name = db.Column(db.String(50), nullable = False)
	date_of_reg = db.Column(db.DateTime(), nullable = False)
	gender = db.Column(db.String(300), nullable = False)
	age = db.Column(db.Integer(), nullable = False)
	#extras for stats
	religion = db.Column(db.String(300), nullable = False)
	civil_status = db.Column(db.String(300), nullable = False)
	educ_attainment = db.Column(db.String(300), nullable = False)
	occupation = db.Column(db.String(300), nullable = False)


