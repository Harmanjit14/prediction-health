from django.db import models
import uuid
# Create your models here.


class UserClass(models.Model):
    name = models.CharField(blank=False, default="User",
                            max_length=255, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return f"User : {self.email}"
