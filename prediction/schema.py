from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


class Query(graphene.ObjectType):
    predict = graphene.List(email=graphene.String())

    def resolve_predict(self, info, email):
        user = UserClass.objects.get(email=email)
        
