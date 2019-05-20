from .. import db


class Dependents(db.Model):
	__tablename__ = "dependents"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	dependents_id = db.Column(db.String(100), unique=True)
	address = db.Column(db.String(300), nullable = False)
	name = db.Column(db.String(50), nullable = False)
	gender = db.Column(db.String(300), nullable = False)
	age = db.Column(db.Integer(), nullable = False)
	educ_attainment = db.Column(db.String(300), nullable = False)
	occupation = db.Column(db.String(300), nullable = False)
	home_id = db.Column(db.Integer(), db.ForeignKey('evacuees.home_id'))
	# center = db.relationship('AssignedCenter')