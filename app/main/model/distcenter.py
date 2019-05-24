from .. import db
from .user import UserAdmin


class DistCenter(db.Model):
	__tablename__ = "distcenter"
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	address = db.Column(db.String(300), nullable = False, unique = True)
	capacity = db.Column(db.Integer(), nullable = False)
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	managed_by = db.Column(db.String(100), db.ForeignKey('useradmin.public_id'), nullable=True, default="None")
	img = db.Column(db.String(300), nullable=True, default="")
	
#class DCManage(db.Model):
#	__tablename__ = "center_manage"
#	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#	admin_id = db.Column(db.String(100), db.ForeignKey('useradmin.public_id'))
#	center_id = db.Column(db.String(100), db.ForeignKey('distcenter.public_id'))
#	
#	admin = db.relationship(UserAdmin, backref=db.backref("manage", cascade="all, delete-orphan"))
#	center = db.relationship(DistCenter, backref=db.backref("manage", cascade="all, delete-orphan"))
