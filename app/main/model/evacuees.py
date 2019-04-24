from .. import db


class Evacuees(db.Model):
	__tablename__ = "evacuees"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	home_id = db.Column(db.Integer(), unique = True)
	address = db.Column(db.String(300), nullable = False)
	date_of_reg = db.Column(db.String(300), nullable = False)
	gender = db.Column(db.String(300), nullable = False)
	age = db.Column(db.Integer(), nullable = False)
	religion = db.Column(db.String(300), nullable = False)
	civil_status = db.Column(db.String(300), nullable = False)
	educ_attainment = db.Column(db.String(300), nullable = False)
	occupation = db.Column(db.String(300), nullable = False)