from django.db import models
from .user import User


class Routine(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    hair_type = models.CharField(max_length=50)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
