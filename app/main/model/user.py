import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key
from .. import db, flask_bcrypt

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    #email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
	middle_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    registered_on = db.Column(db.DateTime(), nullable=False)
    acc_id = db.Column(db.String(100), db.ForeignKey('account.public_id'))
		
class Account(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    pass_hash = db.Column(db.String(100))
    role = db.Column(db.Integer(), db.ForeignKey('role.id'))
	isActive = db.Column(db.Boolean())
    public_id = db.Column(db.String(100), unique=True)
	user = db.relationship('User', backref='account', uselist=False)
    
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.pass_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.pass_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod  
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class Role(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
	account = db.relationship('Account', backref='role', nullable=True)