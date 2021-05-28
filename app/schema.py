import graphene
import users.schema
import meal.schema


class Query(users.schema.Query, meal.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, meal.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
