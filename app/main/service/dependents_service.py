import datetime
import uuid

from app.main import db
from app.main.model.dependents import Dependents
from app.main.model.evacuees import Evacuees
from app.main.model.statistics import StatisticsFemale, StatisticsMale



def save_new_dependents(data):
	dependents = Dependents.query.filter((Dependents.home_id == data["home_id"]) & (Dependents.name == data["name"])).first()
	if not dependents:
		print(data)
		

		new_dependents = Dependents(
			name=data['name'],
			dependents_id=data["home_id"],
			home_id = data['home_id'],
			address=data['address'],
			gender=data['gender'],
			age=data['age'],
			educ_attainment=data['educ_attainment'],
			occupation=data['occupation']
		)
		save_changes(new_dependents)
		response_object = {
			'status' : 'success',
			'message' : 'dependents added'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'dependents id has been already used'
		}
		return response_object, 409


def get_all_dependents():
	return Dependents.query.all()


def get_a_dependent(dependents_id):
	return Dependents.query.filter_by(dependents_id=dependents_id).first()

def delete_dependents(dependents_id):
	dependents = Dependents.query.filter_by(dependents_id=dependents_id).first()
	if dependents:
		db.session.delete(dependents)
		db.session.commit()
		response_object = {
			'status' : 'success',
			'message' : 'dependents deleted'
		}
		return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching dependents found.'
		}
		return response_object, 409


def update_dependent(dependents_id, data):
    # user = UserAdmin.query.filter_by(public_id=public_id).first()
    dependent = db.session.query(Dependents).filter_by(dependents_id=dependents_id).first()
    if dependent:
        dependent.address = data['address']
        dependent.name = data['name']
        dependent.gender = data['gender']
        dependent.age = data['age']
        dependent.educ_attainment = data['educ_attainment']
        dependent.occupation = data['occupation']

        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'Updated Dependent.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'Failed',
            'message': 'No user found'
        }
        return response_object, 409



def save_changes(data):
	db.session.add(data)
	db.session.commit()


def delete_dependents(dependents_id):
	dependents = Dependents.query.filter_by(dependents_id=dependents_id).first()
	if dependents:
			db.session.delete(dependents)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'dependents has been deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'dependents does not exist'
		}
		return response_object, 409



def search_dependent(search_term):
	print(search_term)
	results = Dependents.query.filter(((Dependents.name.like("%"+search_term+"%")) | (Dependents.address.like("%"+search_term+"%")) | (Dependents.gender.like("%"+search_term+"%")) | (Dependents.dependents_id.like("%"+search_term+"%")))).all()
	return results


def get_dependent(home_id):
	results = Dependents.query.filter_by(home_id=home_id).all()
	return results


def remove_dependent(dependents_id, data):
	dependents = Dependents.query.filter((Dependents.home_id == data["home_id"]) & (Dependents.dependents_id == dependents_id)).first()
	if dependents:
		print(dependents)
		dependents.home_id = None

		db.session.commit()
		response_object = {
			'status': 'success',
			'message': 'Remove successfully.'
		}
		return response_object, 201
	else:
		response_object = {
			'status': 'fail',
			'message': 'Dependent does not exist'
		}
		return response_object, 409


def get_age_female():
	all_age = Evacuees.query.with_entities(Evacuees.age).filter_by(gender = "Female").all()
	print(all_age)
	return all_age

def get_age_male():
	all_age = Evacuees.query.with_entities(Evacuees.age).filter_by(gender = "Female").all()
	print(all_age)
	return all_age



def female_age_range(range_age):
	exists = StatisticsFemale.query.filter_by(id=1).first()
	print(exists)
	if exists:
		if range_age == "Gradeschooler":
			check = StatisticsFemale.query.filter_by(id=1).first()
			check_gradeschooler = check.grade_schooler
			print(check_gradeschooler)

			if check_gradeschooler == None:
				check.grade_schooler = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Gradeschooler added'
				}
				return response_object, 201

			else:

				check.grade_schooler = check_gradeschooler + 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Gradeschooler added'
				}
				return response_object, 201

		elif range_age == "Teens":
			check = StatisticsFemale.query.filter_by(id=1).first()
			check_teens = check.teens
			print(check_teens)

			if check_teens == None:
				check.teens = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Teens added'
				}
				return response_object, 201

			else:

				check.teens = check_teens + 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Teens added'
				}
				return response_object, 201

		elif range_age == "Young-Adult":
			check = StatisticsFemale.query.filter_by(id=1).first()
			check_youngadult = check.young_adult
			print(check_youngadult)

			if check_youngadult == None:
				check.young_adult = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Young-Adult added'
				}
				return response_object, 201

			else:

				check.young_adult = check_youngadult+ 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Young-Adult added'
				}
				return response_object, 

		elif range_age == "Adult":
			check = StatisticsFemale.query.filter_by(id=1).first()
			check_adult = check.adult
			print(check_adult)

			if check_adult == None:
				check.adult = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Adult added'
				}
				return response_object, 201

			else:

				check.adult = check_adult+ 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Adult added'
				}
				return response_object, 201
		else:
			response_object = {
				'status': 'fail',
				'message': 'Cannot add range'
			}
			return response_object, 409
	
	else: 

		if range_age == "Gradeschooler":
			new = StatisticsFemale(grade_schooler=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New gradeschooler added'
			}
			return response_object, 201

		elif range_age == "Teens":
			new = StatisticsFemale(teens=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New teens added'
			}
			return response_object, 201

		elif range_age == "Young-Adult":
			new = StatisticsFemale(young_adult=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New young_adult added'
			}
			return response_object, 201

		elif range_age == "Adult":
			new = StatisticsFemale(adult=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New adult added'
			}
			return response_object, 201

		else:
			response_object = {
				'status': 'fail',
				'message': 'Could not add new range'
			}
			return response_object, 409



def male_age_range(range_age):
	exists = StatisticsMale.query.filter_by(id=1).first()
	print(exists)
	if exists:
		if range_age == "Gradeschooler":
			check = StatisticsMale.query.filter_by(id=1).first()
			check_gradeschooler = check.grade_schooler
			print(check_gradeschooler)

			if check_gradeschooler == None:
				check.grade_schooler = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Gradeschooler added - male'
				}
				return response_object, 201

			else:

				check.grade_schooler = check_gradeschooler + 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Gradeschooler added - male'
				}
				return response_object, 201

		elif range_age == "Teens":
			check = StatisticsMale.query.filter_by(id=1).first()
			check_teens = check.teens
			print(check_teens)

			if check_teens == None:
				check.teens = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Teens added - male'
				}
				return response_object, 201

			else:

				check.teens = check_teens + 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Teens added'
				}
				return response_object, 201

		elif range_age == "Young-Adult":
			check = StatisticsMale.query.filter_by(id=1).first()
			check_youngadult = check.young_adult
			print(check_youngadult)

			if check_youngadult == None:
				check.young_adult = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Young-Adult added - male'
				}
				return response_object, 201

			else:

				check.young_adult = check_youngadult+ 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Young-Adult added -male'
				}
				return response_object, 

		elif range_age == "Adult":
			check = StatisticsMale.query.filter_by(id=1).first()
			check_adult = check.adult
			print(check_adult)

			if check_adult == None:
				check.adult = 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Adult added -male'
				}
				return response_object, 201

			else:

				check.adult = check_adult+ 1
				db.session.flush()
				db.session.commit()
				response_object = {
					'status': 'success',
					'message': 'Adult added - male'
				}
				return response_object, 201
		else:
			response_object = {
				'status': 'fail',
				'message': 'Cannot add range'
			}
			return response_object, 409
	
	else: 

		if range_age == "Gradeschooler":
			new = StatisticsMale(grade_schooler=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New gradeschooler added - male'
			}
			return response_object, 201

		elif range_age == "Teens":
			new = StatisticsMale(teens=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New teens added - male'
			}
			return response_object, 201

		elif range_age == "Young-Adult":
			new = StatisticsMale(young_adult=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New young_adult added - male'
			}
			return response_object, 201

		elif range_age == "Adult":
			new = StatisticsMale(adult=1)
			db.session.add(new)
			db.session.commit()

			response_object = {
				'status': 'success',
				'message': 'New adult added - male'
			}
			return response_object, 201

		else:
			response_object = {
				'status': 'fail',
				'message': 'Could not add new range'
			}
			return response_object, 409





