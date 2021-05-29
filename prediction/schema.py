from users.models import UserClass
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q
from meal.models import Meal


class Query(graphene.ObjectType):
    predict = graphene.String(email=graphene.String())

    def resolve_predict(self, info, email):
        avgCarbs = {"low": 225, "high": 325}
        avgproteins = {"low": 35, "high": 64}
        avgfats = {"low": 44, "high": 83}
        avgvitA = {"low": 2000, "high": 3000}
        avgvitD = {"low": 600, "high": 700}
        avgvitC = {"low": 45, "high": 120}
        avgvitE = {"low": 15, "high": 18}
        avgsodium = {"low": 1600, "high": 2800}
        avgiron = {"low": 8.7, "high": 14.8}
        avgpotash = {"low": 4200, "high": 5000}
        avgcalcium = {"low": 1000, "high": 1300}
        avgmag = {"low": 300, "high": 400}
        avgzn = {"low": 8, "high": 11}
        avgPhs = {"low": 700, "high": 1200}
        avgcal = {"low": 1900, "high": 2500}

        avgsleep = 7

        avgbp = {"lessLow": 80, "lessHigh": 120}

        userCarbs = 0
        userproteins = 0
        userfats = 0
        uservitA = 0
        uservitD = 0
        uservitC = 0
        uservitE = 0
        usersodium = 0
        useriron = 0
        userpotash = 0
        usercalcium = 0
        usermag = 0
        userzn = 0
        userPhs = 0
        usercal = 0

        user = UserClass.objects.get(email=email)
        mealdata = Meal.objects.filter(user=user).order_by("-date")[:30]
        if mealdata.count() < 30:
            raise GraphQLError(
                "Complete data for 30 days first before getting Health stats")
        for entry in mealdata:
            userCarbs += float(entry.carbs)
            userproteins += float(entry.proteins)
            usercalcium += float(entry.Calcium)
            usercal += float(entry.omega3)
            userfats += float(entry.fats)
            uservitA += float(entry.vitA)
            uservitE += float(entry.vitE)
            uservitC += float(entry.vitC)
            uservitD += float(entry.vitD)
            usersodium += float(entry.Sodium)
            useriron += float(entry.Iron)
            userpotash += float(entry.Potassium)
            usermag += float(entry.Magnesium)
            userzn += float(entry.Zinc)
            userPhs += float(entry.Phosphorus)

        userCarbs = userCarbs/30
        userproteins = userproteins / 30
        userfats = userfats / 30
        uservitA = uservitA / 30
        uservitD = uservitD / 30
        uservitC = uservitC / 30
        uservitE = uservitE / 30
        usersodium = usersodium / 30
        useriron = useriron / 30
        userpotash = userpotash / 30
        usercalcium = usercalcium / 30
        usermag = usermag / 30
        userzn = userzn / 30
        userPhs = userPhs / 30
        usercal = usercal / 30
        ret = ""
        if userCarbs < avgCarbs.get("low") or userCarbs > avgCarbs.get("high"):
            if userCarbs < avgCarbs.get("low"):
                ret += "Low carbs intake:- impairment of physical activity,lipid abnormalities, and risk of cardiac contractile function impairment \n"
            else:
                ret += "high carbs intake:- Obesity and risk of Non-insulin dependent diabetes\n"

        if userproteins < avgproteins.get("low") or userproteins > avgproteins.get("high"):
            if userproteins < avgproteins.get("low"):
                ret += "Low protein intake:- risk of fatty liver, hair loss, loss of muscle mass\n"
            else:
                ret += "high protein intake:- Constipation, Diarrhea, Dehydration, risk of Kidney damage\n"

        if usercalcium < avgcalcium.get("low") or usercalcium > avgcalcium.get("high"):
            if usercalcium < avgcalcium.get("low"):
                ret += "Low calcium intake:- risk of hypocalcemia\n"
            else:
                ret += "high calcium intake:-risk of Osteoporosis, high risk of Kidney stones\n"

        if uservitA < avgvitA.get("low") or uservitA > avgvitA.get("high"):
            if uservitA < avgvitA.get("low"):
                ret += "Low vit-A intake:- risk of Night Blindness, Infertility and Trouble Conceiving, Throat and Chest Infections, Poor Wound Healing\n"
            else:
                ret += "high vit-A intake:-risk of liver damage, high risk of Kidney damage\n"

        if uservitC < avgvitC.get("low") or uservitC > avgvitC.get("high"):
            if uservitC < avgvitC.get("low"):
                ret += "Low vit-C intake:- pain in the limbs, and especially the legs, risk of scurvy\n"
            else:
                ret += "high vit-C intake:-Headache, risk of Insomnia, Diarrhea, Nausea\n"

        if uservitE < avgvitE.get("low") or uservitE > avgvitE.get("high"):
            if uservitE < avgvitE.get("low"):
                ret += "Low vit-E intake:- short bowel syndrome\n"
            else:
                ret += "high vit-E intake:- risk of blood thinning\n"

        if usersodium < avgsodium.get("low") or usersodium > avgsodium.get("high"):
            if usersodium < avgsodium.get("low"):
                ret += "Low sodium intake:- Headache, Confusion,Loss of energy, drowsiness and fatigue.\n"
            else:
                ret += "high sodium intake:- risk of  high blood pressure, heart disease\n"

        return ret
