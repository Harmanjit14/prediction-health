from .models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


class User(DjangoObjectType):
    class Meta:
        model = UserClass


class Query(graphene.ObjectType):
    getMe = graphene.Field(User, email=graphene.String(required=True))

    def resolve_getMe(self, info, email):
        user = UserClass.objects.get(email=email)
        if user:
            return user
        else:
            raise GraphQLError("No user found")


class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, name, email,**kwargs):
        usr = UserClass.objects.create(email=email, name=name)
        return CreateUser(user=usr)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
