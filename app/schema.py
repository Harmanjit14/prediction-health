import graphene
import users.schema
import meal.schema
import water.schema
import bp.schema


class Query(users.schema.Query, meal.schema.Query,water.schema.Query,bp.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, meal.schema.Mutation,water.schema.Mutation,bp.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
