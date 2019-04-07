from flask import Blueprint
from flask_restplus import Api

from app.apis.user import api as ns1
from app.apis.post import api as ns2

blueprint = Blueprint('api', __name__, url_prefix='/api/v2')
api = Api(blueprint)

api.add_namespace(ns1)
api.add_namespace(ns2)