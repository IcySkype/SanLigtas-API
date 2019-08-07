from .. import db
from .distcenter import DistCenter


class RGoods(db.Model):
	__tablename__ = "goods"
	#Relief Goods basic data
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	#goods public identifier
	code = db.Column(db.String(300), nullable = False, unique=True)
	#cash/consumable/clothing
	type = db.Column(db.String(300), nullable = False)
	status = db.Column(db.String(300), nullable = False)
	amount = db.Column(db.Integer(), nullable = False)

	#Goods distribution data
	center_id = db.Column(db.String(100), db.ForeignKey('distcenter.public_id'), nullable=True)
	received_date = db.Column(db.String(300), nullable = False)
	received_from = db.Column(db.String(300), nullable = False)
	distribute_date = db.Column(db.String(300), nullable = True, default=None)
	
	#optional: food
	expiry = db.Column(db.String(300), nullable = True, default = None)
	#optional: clothing
	size = db.Column(db.String(5), nullable = False, default=None)
	clothing_type = db.Column(db.String(300), nullable = False, default=None)
	condition = db.Column(db.String(300), nullable = False, default=None)