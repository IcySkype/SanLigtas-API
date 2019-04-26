from .. import db


class Evacuees(db.Model):
	__tablename__ = "evacuees"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	home_id = db.Column(db.Integer(), unique = True)
	dependents_id = db.Column(db.Integer(), db.ForeignKey('dependents.dependents_id'))
	name = db.Column(db.String(50), nullable = False)
	address = db.Column(db.String(300), nullable = False)
	date_of_reg = db.Column(db.DateTime(), nullable = False)
	gender = db.Column(db.String(300), nullable = False)
	age = db.Column(db.Integer(), nullable = False)
	religion = db.Column(db.String(300), nullable = False)
	civil_status = db.Column(db.String(300), nullable = False)
	educ_attainment = db.Column(db.String(300), nullable = False)
	occupation = db.Column(db.String(300), nullable = False)