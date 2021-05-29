from .models import Cholestrol
from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


class Usercholestrol(DjangoObjectType):
    class Meta:
        model = Cholestrol


class Query(graphene.ObjectType):
    getUserChData = graphene.List(
        Usercholestrol, email=graphene.String(required=True))

    def resolve_getUserChData(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        return Cholestrol.objects.filter(user=user).order_by("-date")[:30]


class AddCholestrol(graphene.Mutation):
    newch = graphene.Field(Usercholestrol)

    class Arguments:
        email = graphene.String()
        cholestrollevel = graphene.Float()

    def mutate(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        ch = Cholestrol.objects.create(user=user,
                                       cholestrollevel=kwargs.get("cholestrollevel"))
        return AddCholestrol(newsleep=ch)


class Mutation(graphene.ObjectType):
    add_ch = AddCholestrol.Field()
