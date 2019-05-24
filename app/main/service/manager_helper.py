from app.main.model.user import UserAdmin
from app.main.model.distcenter import DistCenter
from app.main import db

class ManageCenter:
	@staticmethod
	def assign_admin(admin_id, dc_id):
		try:
			user = UserAdmin.query.filter_by(public_id=admin_id).first()
			dc = DistCenter.query.filter_by(public_id=dc_id).first()
			role = user.role.lower()
			isMain = "main admin" in role
			if not isMain and not manages:
			#if admin is not main admin and not currently managing a center, add
				dc.managed_by = admin_id
				db.session.commit()
				response_object = {
						'status' : 'success',
						'message' : 'Admin is now assigned.'
					}
				return response_object, 200
			elif isMain:
			#if admin is main admin, add
				dc.managed_by = admin_id
				db.session.commit()
				response_object = {
						'status' : 'success',
						'message' : 'Main Admin is now assigned.'
					}
				return response_object, 200
			else:
			#if not main admin and currently manages a center, deny
				response_object = {
						'status' : 'Fail',
						'message' : 'Admin already managing a center.'
					}
				return response_object, 401
		except Exception as e:
			print(e)
			response_object = {
				'status' : 'fail',
				'message' : 'Try again'
			}
			return response_object, 500	
	
	@staticmethod
	def unassign_admin(admin_id, dc_id):
		user = UserAdmin.query.filter_by(public_id=admin_id).first()
		dc = DistCenter.query.filter_by(public_id=dc_id).first()
		if dc and user:
			dc.managed_by = "None"
			db.session.commit()
			response_object = {
				'status' : 'success',
				'message' : 'Admin is now unassigned to this center.'
			}
			return response_object, 200
		else:
			response_object = {
				'status' : 'fail',
				'message' : 'No such relation exists.'
			}
			return response_object, 401
	
	@staticmethod		
	def assigned_centers(admin_id):
		user = UserAdmin.query.filter_by(public_id=admin_id).first()
		return user.manages
		
	@staticmethod		
	def manager_of(dc_id):
		dc = DistCenter.query.filter_by(public_id=dc_id).first()
		user = UserAdmin.query.filter_by(public_id=dc.managed_by).first()
		return (user)