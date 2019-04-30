from .. import db


class DistCenter(db.Model):
	__tablename__ = "distcenter"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	address = db.Column(db.String(300), nullable = False, unique = True)
	capacity = db.Column(db.Integer(), nullable = False)
	public_id = db.Column(db.String(300), nullable = False)

