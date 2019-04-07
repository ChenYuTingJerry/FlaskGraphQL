from app.db import mongodb
from flask import current_app as app
db = mongodb.engine


class Comment(db.EmbeddedDocument):
    content = db.StringField()
    name = db.StringField(max_length=120)


class UserModel(db.Document):
    email = db.EmailField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    posts = db.ListField(db.ReferenceField('app.models.PostModel'))

    def to_dict(self):
        app.logger.info(f'{[str(post.id) for post in self.posts]}')
        return {
            'id': str(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'posts': [str(post.id) for post in self.posts]
        }


class PostModel(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(UserModel)
    tags = db.ListField(db.StringField(max_length=30))
    comments = db.ListField(db.EmbeddedDocumentField(Comment))

    # bugfix
    meta = {'allow_inheritance': True}

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'author': str(self.author.id),
            'tags': self.tags,
            'comments': self.comments
        }


class TextPostModel(PostModel):
    content = db.StringField()

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'author': str(self.author.id),
            'tags': self.tags,
            'comments': self.comments,
            'content': self.content
        }


class ImagePostModel(PostModel):
    image_path = db.StringField()

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'author': str(self.author.id),
            'tags': self.tags,
            'comments': self.comments,
            'image_path': self.image_path
        }


class LinkPostModel(PostModel):
    link_url = db.URLField()

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'author': str(self.author.id),
            'tags': self.tags,
            'comments': self.comments,
            'link_url': self.link_url
        }
