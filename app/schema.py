import graphene
from app.models import UserModel, PostModel


class User(graphene.ObjectType):
    id = graphene.ID()
    last_name = graphene.String()
    first_name = graphene.String()
    email = graphene.String()
    posts = graphene.List('app.schema.Post')


class Post(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.Field(User)
    tags = graphene.List(graphene.String)
    link_url = graphene.String()
    content = graphene.String()
    image_path = graphene.String()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    posts = graphene.List(Post)
    user = graphene.Field(User, id=graphene.String())
    user_specific_posts = graphene.Field(User, id=graphene.String(), tag=graphene.String())

    def resolve_users(self, info):
        return UserModel.objects()

    def resolve_posts(self, info):
        return PostModel.objects()

    def resolve_user(self, info, id):
        return UserModel.objects().get(id=id)


schema = graphene.Schema(query=Query, types=[Post, User])
