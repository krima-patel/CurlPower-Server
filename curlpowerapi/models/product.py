from django.db import models
from .user import User
from .routine import Routine

class Product(models.Model):

    routine = models.ForeignKey(Routine, on_delete = models.CASCADE)
    hair_type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    purpose = models.TextField()
    price_range = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
