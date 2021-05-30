from .models import Meal
from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q
from datetime import date
from django.utils.timezone import now

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
        m = Meal.objects.filter(user=user, date=date.today()).count()
        if m>0:
            m = Meal.objects.filter(user=user, date=date.today())[0]
            m.carbs += float(kwargs.get("carbs", 0))
            m.proteins += float(kwargs.get("proteins", 0))
            m.fats += float(kwargs.get("fats", 0))
            m.vitA += float(kwargs.get("vitA", 0))
            m.vitC += float(kwargs.get("vitC", 0))
            m.vitD += float(kwargs.get("vitD", 0))
            m.vitE += float(kwargs.get("vitE", 0))
            m.Sodium += float(kwargs.get("Sodium", 0))
            m.Iron += float(kwargs.get("Iron", 0))
            m.Potassium += float(kwargs.get("Potassium", 0))
            m.Calcium += float(kwargs.get("Calcium", 0))
            m.Magnesium += float(kwargs.get("Magnesium", 0))
            m.Zinc += float(kwargs.get("Zinc", 0))
            m.Phosphorus += float(kwargs.get("Phosphorus", 0))
            m.omega3 += float(kwargs.get("omega3", 0))
            m.save()
        else:
            m = Meal.objects.create(user=user, carbs=kwargs.get("carbs"), proteins=kwargs.get("proteins"),
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
