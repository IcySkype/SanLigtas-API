from flask_restplus import Api
from flask import Blueprint

from .main.controller.useradmin_controller import api as useradmin_ns
from .main.controller.usermobile_controller import api as usermobile_ns
from .main.controller.authadmin_controller import api as authadmin_ns
from .main.controller.authmobile_controller import api as authmobile_ns
from .main.controller.distcenter_controller import api as dcenter_ns
from .main.controller.evacuees_controller import api as evacuee_ns
from .main.controller.household_controller import api as house_ns
from .main.controller.manage_controller import api as manage_center_ns
from .main.controller.upload_controller import api as upload_ns
from .main.controller.goods_controller import api as rgoods_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
	title='SANLIGTAS API USING FLASK RESTPLUS',
	version='1.0',
	description='sanligtas api run on flask restplus'
)

api.add_namespace(useradmin_ns, path='/user/admin')
api.add_namespace(usermobile_ns, path='/user/mobile')
api.add_namespace(authadmin_ns)
api.add_namespace(authmobile_ns)
api.add_namespace(dcenter_ns, path='/center')
api.add_namespace(evacuee_ns, path='/evacuees')
api.add_namespace(house_ns, path='/house')
api.add_namespace(manage_center_ns)
api.add_namespace(upload_ns)
api.add_namespace(rgoods_ns, path='/rgoods')

