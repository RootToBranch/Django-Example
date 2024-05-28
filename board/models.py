from django.db import models

class TempUser(models.Model):
    username = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField(default=0)