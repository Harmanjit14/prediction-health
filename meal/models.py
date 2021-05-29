from django.db import models
from users.models import UserClass
import uuid
from django.utils.timezone import now
# Create your models here.


class Meal(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    date = models.DateField(editable=True,auto_now_add=True)
    date.editable=True
    carbs = models.FloatField(default=0, blank=False)
    proteins = models.FloatField(default=0, blank=False)
    fats = models.FloatField(default=0, blank=False)
    vitA = models.FloatField(default=0, blank=False)
    vitD = models.FloatField(default=0, blank=False)
    vitC = models.FloatField(default=0, blank=False)
    vitE = models.FloatField(default=0, blank=False)
    Sodium = models.FloatField(default=0, blank=False)
    Iron = models.FloatField(default=0, blank=False)
    Potassium = models.FloatField(default=0, blank=False)
    Calcium = models.FloatField(default=0, blank=False)
    Magnesium = models.FloatField(default=0, blank=False)
    Zinc = models.FloatField(default=0, blank=False)
    Phosphorus = models.FloatField(default=0, blank=False)
    omega3 = models.FloatField(default=0, blank=False)

    def __str__(self):
        return f"Meal id : {self.id}"
