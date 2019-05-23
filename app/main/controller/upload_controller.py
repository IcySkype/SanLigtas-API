import os, werkzeug

from flask import request, send_from_directory, jsonify, abort, send_file
from flask_restplus import Resource, Namespace



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
		print (filename)
		if "/" in filename:
			abort(400, "Bad Request")
		
		destination = "/".join([img_folder, filename])
		#file = r'%s%s' % (img_folder, filename.filename+'.png')
		args['file'].save(destination)
		
#		with open(os.path.join(img_folder, filename), "wb") as fp:
#			fp.write(request.form)
			
		return "Done", 201
