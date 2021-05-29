from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


class Query(graphene.ObjectType):
    predict = graphene.String(email=graphene.string())

    def resolve_predict(self, info, email):
        avgCarbs = {"low": 225, "high": 325}
        avgproteins = {"low": 42, "high": 54}
        avgfats = {"low": 44, "high": 77}
        avgvitA = {"low": 0.0007, "high": 0.0009}
        avgvitD = {"low": 0.0000375, "high": 0.00005}
        avgvitC = {"low": 42, "high": 54}
        user = UserClass.objects.get(email=email)
        ret = ""
