import datetime
from sqlalchemy.orm import load_only


from app.main import db
from app.main.model.evacuees import Evacuees
from app.main.model.statistics import StatisticsFemale, StatisticsMale




def add_evacuee(data):
	print(data)
	evacuee = Evacuees.query.filter((Evacuees.home_id == data["home_id"]) & (Evacuees.center_id == data["center_id"])).first()

	if not evacuee:
		evacuee = Evacuees.query.filter_by(home_id=data["home_id"]).first()

		evacuee.center_id=data["center_id"]

		db.session.commit()

		response_object = {
			'status': 'success',
			'message': 'Evacuee successfully assigned'
		}
		return response_object, 200
	else:
		response_object = {
			'status': 'fail',
			'message': 'Evacuee already assigned.'
		}
		return response_object, 409



def save_new_evacuees(data):
	evacuees = Evacuees.query.filter_by(home_id=data['home_id']).first()
	if not evacuees:
		new_evacuees = Evacuees(
			name=data['name'],
			home_id=data['home_id'],
			date_of_reg=datetime.datetime.utcnow(),
			address=data['address'],
			gender=data['gender'],
			age=data['age'],
			religion=data['religion'],
			civil_status=data['civil_status'],
			educ_attainment=data['educ_attainment'],
			occupation=data['occupation']
		)
		print (new_evacuees) 
		save_changes(new_evacuees)
		response_object = {
			'status' : 'success',
			'message' : 'evacuees added'
		}
		return response_object, 201
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'home id has been already used'
		}
		return response_object, 409


def get_all_evacuees():
	return Evacuees.query.all()


def get_a_evacuee(home_id):
	return Evacuees.query.filter_by(home_id=home_id).first()


def delete_evacuees(home_id):
	evac = Evacuees.query.filter_by(home_id=home_id).first()
	if dcenter:
			db.session.delete(evac)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'Evacuee deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'No matching evacuee found.'
		}
		return response_object, 409
		


def update_evacuees(home_id, data):
    evacuee = db.session.query(Evacuees).filter_by(home_id=home_id).first()
    if evacuee:
        evacuee.name = data['name']
        evacuee.address = data['address']
        evacuee.gender = data['gender']
        evacuee.age = data['age']
        evacuee.religion = data['religion']
        evacuee.civil_status = data['civil_status']
        evacuee.educ_attainment = data['educ_attainment']
        evacuee.occupation = data['occupation']

        db.session.commit()
        response_object = {
            'status': 'Success',
            'message': 'Updated Evacuee.'
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



def delete_evacuees(home_id):
	evacuees = Evacuees.query.filter_by(home_id=home_id).first()
	if evacuees:
			db.session.delete(evacuees)
			db.session.commit()
			response_object = {
			'status' : 'success',
			'message' : 'evacuee has been deleted'
			}
			return response_object, 204
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'evacuee does not exist'
		}
		return response_object, 409



def search_evacuee(search_term):
	print(search_term)
	results = Evacuees.query.filter(((Evacuees.name.like("%"+search_term+"%")) | (Evacuees.address.like("%"+search_term+"%")) | (Evacuees.gender.like("%"+search_term+"%")))).all()
	return results


def get_center_center_id(center_id):
	print(center_id)
	results = Evacuees.query.filter_by(center_id=center_id).all()
	return results


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





