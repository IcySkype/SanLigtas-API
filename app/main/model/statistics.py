from .. import db


class StatisticsFemale(db.Model):
	__tablename__ = "statisticsfemale"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	grade_schooler = db.Column(db.Integer())
	teens = db.Column(db.Integer())
	young_adult = db.Column(db.Integer())
	adult = db.Column(db.Integer())
	

class StatisticsMale(db.Model):
	__tablename__ = "statisticsmale"

	id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
	grade_schooler = db.Column(db.Integer())
	teens = db.Column(db.Integer())
	young_adult = db.Column(db.Integer())
	adult = db.Column(db.Integer())
	