from .. import db



class Dependents(db.Model):
	__tablename__ = "dependents"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	dependents_id = db.Column(db.Integer(), unique = True)
	name = db.Column(db.String(50), nullable = False)
	address = db.Column(db.String(300), db.ForeignKey('evacuees.address'))
	gender = db.Column(db.String(300), nullable = False)
	age = db.Column(db.Integer(), nullable = False)
	educ_attainment = db.Column(db.String(300), nullable = False)
	occupation = db.Column(db.String(300), nullable = False)