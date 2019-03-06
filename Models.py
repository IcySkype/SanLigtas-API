from config import db

class User(db.Model):
	#attributes
	__tablename__ = 'Users'
	id = db.Column('user_id', db.Integer())
	username = db.Column('username', db.String(), unique=True)
	pass_hash = db.Column('pass', db.String())

	#methods
	def __init__(self, attributes):
		self.attributes setup

	def hash_pass(self, pass):
		self.pass_hash = pwd_context.encrypt(pass)

	def verify_pass(self, pass):
		return pwd_context.verify(pass, self.pass_hash)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return self.username

	@property
	def serialize(self):
		return {
			'id'		: self.id
			'username'	: self.username
			'pass_hash'	: self.pass_hash
		}
