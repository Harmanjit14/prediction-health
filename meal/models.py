from django.db import models
from users.models import UserClass
import uuid
from django.utils.timezone import now
# Create your models here.


class Meal(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    carbs = models.FloatField(default=0, blank=False, null=True)
    proteins = models.FloatField(default=0, blank=False, null=True)
    fats = models.FloatField(default=0, blank=False, null=True)
    vitA = models.FloatField(default=0, blank=False, null=True)
    vitD = models.FloatField(default=0, blank=False, null=True)
    vitC = models.FloatField(default=0, blank=False, null=True)
    vitE = models.FloatField(default=0, blank=False, null=True)
    Sodium = models.FloatField(default=0, blank=False, null=True)
    Iron = models.FloatField(default=0, blank=False, null=True)
    Potassium = models.FloatField(default=0, blank=False, null=True)
    Calcium = models.FloatField(default=0, blank=False, null=True)
    Magnesium = models.FloatField(default=0, blank=False, null=True)
    Zinc = models.FloatField(default=0, blank=False, null=True)
    Phosphorus = models.FloatField(default=0, blank=False, null=True)
    omega3 = models.FloatField(default=0, blank=False, null=True)

    def __str__(self):
        return f"Meal id : {self.id}"
