from .. import db


class House(db.Model):
	__tablename__ = "household"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	address = db.Column(db.String(300), nullable = False, unique=True)
	public_id = db.Column(db.String(300), nullable = False, unique=True)