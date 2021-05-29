from django.db import models
from users.models import UserClass
import uuid



class DailySpo2(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    level = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f"Spo2level id : {self.id}"
