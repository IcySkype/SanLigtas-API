from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.distcenter_controller import api as dcenter_ns
from .main.controller.evacuees_controller import api as evacuee_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
	title='SANLIGTAS API USING FLASK RESTPLUS',
	version='1.0',
	description='sanligtas api run on flask restplus'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(dcenter_ns)
api.add_namespace(evacuee_ns)

