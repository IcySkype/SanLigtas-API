from .. import db


class DistCenter(db.Model):
	__tablename__ = "distcenter"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable = False)
	address = db.Column(db.String(300), nullable = False, unique = True)
	capacity = db.Column(db.Integer(), nullable = False)
	public_id = db.Column(db.String(300), nullable = False, unique=True)
	longitude = db.Column(db.FLOAT, nullable=False)
	latitude = db.Column(db.FLOAT, nullable=False)
	useradmin_id = db.Column(db.Integer(), db.ForeignKey('useradmin.id'))


class AssignedCenter(db.Model):
	__tablename__ = "assignedcenter"

	center_id = db.Column(db.Integer(), primary_key=True)
	center_public_id = db.Column(db.String(300), nullable=False)
	center_admin = db.Column(db.String(50), db.ForeignKey('useradmin.username'))
	# evacuees_id = db.Column(db.Integer, db.ForeignKey('evacuees.id'))
	# dependents_contain = db.relationship('Dependents', backref='contain_dependents', lazy='dynamic', primaryjoin=" == Dependents.id")
	# evacuees_contain = db.relationship('Evacuees', backref=db.backref('contain_evacuees'))	
