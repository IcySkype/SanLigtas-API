import os, werkzeug

from flask import request, send_from_directory, jsonify, abort, send_file
from flask_restplus import Resource, Namespace

from ..util.decoratoradmin import token_required
from app.main.model.user import UserAdmin
from app.main.model.distcenter import DistCenter
from app.main import db

api = Namespace('files', description='File Related')
parser = api.parser()
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

img_folder = 'app/static/uploads/img'


if not os.path.exists(img_folder):
	os.makedirs(img_folder)

@api.route('/')
class AllPictures(Resource):
	@api.doc('get all uploads')
	def get(self):
		files = []
		for filename in os.listdir(img_folder):
			path = os.path.join(img_folder, filename)
			if os.path.isfile(path):
				files.append(filename)
		return jsonify(files)


@api.route('/<path:path>')
class FileDL(Resource):
#working example path: ..\static\uploads\img\image.png
	@api.doc('download file')
	def get(self, path):
		try:
			return send_file(path, as_attachment=True)
		except Exception as e:
			print(e)
			abort(400)
		
@api.route('/upload/')
class FileUP(Resource):
	@api.doc('upload a file', parser=parser)
	def post(self):
		args = parser.parse_args()
		filename = args['file'].filename
		if "/" in filename:
			abort(400, "Bad Request")
		
		destination = "/".join([img_folder, filename])
		#file = r'%s%s' % (img_folder, filename.filename+'.png')
		args['file'].save(destination)
		
#		with open(os.path.join(img_folder, filename), "wb") as fp:
#			fp.write(request.form)
			
		return "Done", 201

@api.route('/upload/user/<public_id>')
class FileUpUser(Resource):
	@api.doc('Upload a file, personal to user', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self, public_id):
		args = parser.parse_args()
		filename = args['file'].filename
		if "/" in filename:
			abort(400, "Bad Request")
		
		user_folder = img_folder+'/user/'+public_id
		if not os.path.exists(user_folder):
			os.makedirs(user_folder)
		
		destination = "/".join([user_folder, filename])
		args['file'].save(destination)
		
		user = UserAdmin.query.filter_by(public_id=public_id).first()
		user.img = filename
		
		return "Done", 201
		
@api.route('/upload/center/<public_id>')
class FileUpUser(Resource):
	@api.doc('Upload a file, personal to user', parser=parser)
	@api.header('Authorization', 'JWT TOKEN', required=True)
	@token_required
	def post(self, public_id):
		args = parser.parse_args()
		filename = args['file'].filename
		if "/" in filename:
			abort(400, "Bad Request")
		
		center_folder = img_folder+'/center/'+public_id
		if not os.path.exists(center_folder):
			os.makedirs(center_folder)
			
		destination = "/".join([center_folder, filename])
		args['file'].save(destination)
		
		dc = DistCenter.query.filter_by(public_id=public_id).first()
		dc.img = filename
		
		return "Done", 201