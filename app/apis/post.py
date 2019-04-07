from flask_restplus import Namespace, Resource
from app.models import PostModel

api = Namespace('posts', description='Post')


@api.route('/')
class PostList(Resource):
    @api.doc('list_posts')
    def get(self):
        '''List all users'''
        return [obj.to_dict() for obj in PostModel.objects]


@api.route('/<id>')
@api.param('id', 'The post identifier')
@api.response(404, 'Post not found')
class User(Resource):
    @api.doc('get_post')
    def get(self, id):
        '''Fetch a cat given its identifier'''
        return PostModel.objects.get(id=id).to_dict()
