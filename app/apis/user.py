from flask_restplus import Namespace, Resource
from app.models import UserModel

api = Namespace('users', description='User')


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    def get(self):
        '''List all users'''
        return [obj.to_dict() for obj in UserModel.objects]


@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    def get(self, id):
        '''Fetch a cat given its identifier'''
        return UserModel.objects.get(id=id).to_dict()
