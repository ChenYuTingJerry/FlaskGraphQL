from flask_mongoengine import MongoEngine
from flask import current_app as app

__all__ = ['mongodb']


class DatabaseProxy:
    def init(self, app):
        raise NotImplemented('init_db() needs to be implemented')

    @property
    def engine(self):
        raise NotImplemented('engine() needs to be implemented')

    def commit(self):
        raise NotImplemented('commit() needs to be implemented')

    def rollback(self):
        raise NotImplemented('rollback() needs to be implemented')


_engines = {
    'mongo': MongoEngine()
}


class Mongodb(DatabaseProxy):
    def __init__(self):
        self.db = _engines.get('mongo')

    def init(self, app):
        self.db.init_app(app)

    @property
    def engine(self):
        return self.db


def init_db():
    from app.models import PostModel, UserModel, TextPostModel, LinkPostModel
    PostModel.drop_collection()
    UserModel.drop_collection()

    user1 = UserModel(email='jdoe@example.com', first_name='John', last_name='Doe')
    user1.save()

    post1 = TextPostModel(title='Fun with MongoEngine', author=user1)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

    post2 = LinkPostModel(title='MongoEngine Documentation', author=user1)
    post2.link_url = 'http://tractiondigital.com/labs/mongoengine/docs'
    post2.tags = ['mongoengine']
    post2.save()


    user2 = UserModel(email='jessica@example.com', first_name='Jessica', last_name='Jones')
    user2.save()

    post1 = TextPostModel(title='How to develop a Flask, GraphQL, Graphene, MySQL, and Docker starter kit', author=user2)
    post1.content = 'Up until now, I have mostly been developing new Flask projects from scratch. As most projects tend to consist of similar folder structures, it gets really mundane setting up the identical base projects repeatedly over a period of time.'
    post1.tags = ['graphene', 'flask']
    post1.save()

    post2 = LinkPostModel(title='An introduction to RabbitMQ, a broker that deals in messages', author=user2)
    post2.link_url = 'https://medium.freecodecamp.org/rabbitmq-9e8f78194993'
    post2.tags = ['rabbitmq']
    post2.save()

    user2.posts.append(post1.id)
    user2.posts.append(post2.id)
    user2.save()
    # num_posts = Post.objects(tags='mongodb').count()
    # app.logger.info('Found %d posts with tag "mongodb"' % num_posts)


mongodb = Mongodb()
