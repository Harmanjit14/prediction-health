from .models import DailySpo2
from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


class UserSPO2(DjangoObjectType):
    class Meta:
        model = DailySpo2


class Query(graphene.ObjectType):
    getUserSPO2Data = graphene.List(
        UserSPO2, email=graphene.String(required=True))

    def resolve_getUserSPO2Data(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        return DailySpo2.objects.filter(user=user).order_by("-date")[:30]


class AddSPO2(graphene.Mutation):
    newlevel = graphene.Field(UserSPO2)

    class Arguments:
        email = graphene.String()
        level = graphene.Int()

    def mutate(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        s = DailySpo2.objects.create(user=user,
                                     level=kwargs.get("level"),
                                     )
        return AddSPO2(newlevel=s)


class Mutation(graphene.ObjectType):
    add_spo2 = AddSPO2.Field()
