from .. import db
from .distcenter import DistCenter

class Goods(db.Model):
	__tablename__ = "goods"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable = False)
	details = db.Column(db.String(300), nullable = True)
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	type = db.Column(db.Integer(), db.ForeignKey('good_type.id'))
	amount = db.Column(db.Integer(), nullable = False)
	received_date = db.Column(db.String(300), nullable = False)
	distribute_date = db.Column(db.String(300), nullable = True)
	status = db.Column(db.String(50), nullable = True)
	isActive = db.Column(db.Boolean(), nullable = False)
	center_id = db.Column(db.String(300), db.ForeignKey('distcenter.public_id'))
	
class GoodType(db.Model):
	__tablename__ = "good_type"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	rgood = db.relationship('Goods', backref='good_type')

