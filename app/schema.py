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
    user = graphene.Field(User, email=graphene.String())
    user_specific_posts = graphene.Field(User, id=graphene.String(), tag=graphene.String())

    def resolve_users(self, info):
        return UserModel.objects()

    def resolve_posts(self, info):
        return PostModel.objects()

    def resolve_user(self, info, email):
        return UserModel.objects().get(email=email)


class CreateUser(graphene.Mutation):
    id = graphene.ID()
    last_name = graphene.String()
    first_name = graphene.String()
    email = graphene.String()
    posts = graphene.List('app.schema.Post')

    class Arguments:
        email = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, email, first_name, last_name, user_id=None):
        user = UserModel(email=email, first_name=first_name, last_name=last_name)
        if user_id:
            user.id = user_id
        user.save()
        return CreateUser(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Post, User])
