from .models import WaterIntake
from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

class UserWater(DjangoObjectType):
    class Meta:
        model = WaterIntake


class Query(graphene.ObjectType):
    getUserWaterData = graphene.List(
        UserWater, email=graphene.String(required=True))

    def resolve_getUserWaterData(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        return WaterIntake.objects.filter(user=user).order_by("-date")[:30]


class AddWater(graphene.Mutation):
    water = graphene.Field(UserWater)

    class Arguments:
        email = graphene.String()
        name = graphene.String()
        quantitylitre = graphene.Int()

    def mutate(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        w = WaterIntake.objects.create(user=user, 
            quantitylitre=kwargs.get("quantitylitre"))
        return AddWater(water=w)


class Mutation(graphene.ObjectType):
    add_water = AddWater.Field()