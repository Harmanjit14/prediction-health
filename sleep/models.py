from django.db import models
from users.models import UserClass
import uuid



class Sleep(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    sleephours = models.FloatField(default=0, blank=False)

    def __str__(self):
        return f"Sleephours id : {self.id}"