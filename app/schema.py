import graphene
import users.schema
import meal.schema
import water.schema
import bp.schema
import sleep.schema
import cholestrol.schema


class Query(users.schema.Query, meal.schema.Query,water.schema.Query,bp.schema.Query,sleep.schema.Query, cholestrol.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, meal.schema.Mutation,water.schema.Mutation,bp.schema.Mutation,sleep.schema.Mutation, cholestrol.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
