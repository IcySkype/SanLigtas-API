from .. import db

manage = db.Table('manage',
	db.Column('center_id', db.String(300), db.ForeignKey('distcenter.public_id')),
	db.Column('acc_id', db.String(300), db.ForeignKey('account.public_id'))
)

class DistCenter(db.Model):
	__tablename__ = "distcenter"
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), unique=True, nullable = False)
	barangay_id = db.Column(db.Integer(), db.ForeignKey('barangay.id'))
	capacity = db.Column(db.Integer(), nullable = False)
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	evacs = db.relationship('Evacuees', backref='center')
	managers = db.relationship('Account', secondary=manage, backref=db.backref('centers', lazy = 'dynamic'))
	
class Barangay(db.Model):
	__tablename__ = "barangay"
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	center = db.relationship('DistCenter', backref='barangay')
	evacuees = db.relationship('Evacuees', backref='barangay')
	
