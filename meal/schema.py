from .models import Meal
from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


class UserMeals(DjangoObjectType):
    class Meta:
        model = Meal


class Query(graphene.ObjectType):
    getUserMealData = graphene.List(
        UserMeals, email=graphene.String(required=True))

    def resolve_getUserMealData(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        return Meal.objects.filter(user=user).order_by("-date")[:30]


class AddMeal(graphene.Mutation):
    meal = graphene.Field(UserMeals)

    class Arguments:
        email = graphene.String()
        name = graphene.String()
        carbs = graphene.Float()
        proteins = graphene.Float()
        fats = graphene.Float()
        vitA = graphene.Float()
        vitD = graphene.Float()
        vitC = graphene.Float()
        vitE = graphene.Float()
        Sodium = graphene.Float()
        Iron = graphene.Float()
        Potassium = graphene.Float()
        Calcium = graphene.Float()
        Magnesium = graphene.Float()
        Zinc = graphene.Float()
        Phosphorus = graphene.Float()
        omega3 = graphene.Float()

    def mutate(self, info, **kwargs):
        user = UserClass.objects.get(email=kwargs.get("email"))
        if user is None:
            raise GraphQLError("No user found")
        m = Meal.objects.create(user=user, meal_name=kwargs.get(
            "name"), carbs=kwargs.get("carbs"), proteins=kwargs.get("proteins"),
            fats=kwargs.get("fats"), vitA=kwargs.get("vitA"),
            vitC=kwargs.get("vitC"), vitD=kwargs.get("vitD"),
            vitE=kwargs.get("vitE"), Sodium=kwargs.get("Sodium"),
            Iron=kwargs.get("Iron"), Potassium=kwargs.get("Potassium"),
            Calcium=kwargs.get("Calcium"),
            Magnesium=kwargs.get("Magnesium"),
            Zinc=kwargs.get("Zinc"),
            Phosphorus=kwargs.get("Phosphorus"),
            omega3=kwargs.get("omega3"))
        return AddMeal(meal=m)


class Mutation(graphene.ObjectType):
    add_meal = AddMeal.Field()
