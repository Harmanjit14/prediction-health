from .models import Sleep
from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


class UserSleep(DjangoObjectType):
    class Meta:
        model = Sleep


class Query(graphene.ObjectType):
    getUserSleepData = graphene.List(
        UserSleep, email=graphene.String(required=True))

    def resolve_getUserSleepData(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        return Sleep.objects.filter(user=user).order_by("-date")[:30]


class AddSleep(graphene.Mutation):
    newsleep = graphene.Field(UserSleep)

    class Arguments:
        email = graphene.String()
        sleephours = graphene.Int()

    def mutate(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        s = Sleep.objects.create(user=user,
                                 sleephours=kwargs.get("sleephours"))
        return AddSleep(newsleep=s)


class Mutation(graphene.ObjectType):
    add_sleep = AddSleep.Field()
