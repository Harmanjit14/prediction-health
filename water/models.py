from django.db import models
from users.models import UserClass
import uuid



class WaterIntake(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    quantitylitre = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f"WaterIntake id : {self.id}"



