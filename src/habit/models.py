from django.conf import settings
from django.db import models


class Habit(models.Model):
    name = models.TextField()
    description = models.TextField(
        help_text="A short description about what you want to achieve"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
