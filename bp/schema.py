from .models import DailyBp
from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

class UserBP(DjangoObjectType):
    class Meta:
        model = DailyBp


class Query(graphene.ObjectType):
    getUserBPData = graphene.List(
        UserBP, email=graphene.String(required=True))

    def resolve_getUserBPData(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        return DailyBp.objects.filter(user=user).order_by("-date")[:30]


class AddBP(graphene.Mutation):
    newbp = graphene.Field(UserBP)

    class Arguments:
        email = graphene.String()
        name = graphene.String()
        systolic = graphene.Float()
        diastolic = graphene.Float()

    def mutate(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        b = DailyBp.objects.create(user=user, 
            systolic=kwargs.get("systolic"),
            diastolic=kwargs.get("diastolic"),
            )
        return AddBP(newbp=b)


class Mutation(graphene.ObjectType):
    add_bp = AddBP.Field()