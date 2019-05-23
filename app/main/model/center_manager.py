from .. import db


class DistCenter(db.Model):
	__tablename__ = "centermanager"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	manager = db.Column(db.String(300), nullable = False)
	center = db.Column(db.String(300), nullable = False)