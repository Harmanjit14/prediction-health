import graphene
import users.schema


class Query(users.schema.Query, graphene.ObjectType):
    pass


# class Mutation( graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)
