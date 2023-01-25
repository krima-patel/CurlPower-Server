from django.db import models
from .routine import Routine
from .user import User

class Product(models.Model):

    routine = models.ForeignKey(Routine, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    purpose = models.TextField()
    price_range = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    @property
    def types(self):
        """Will be used to return hair types of products"""
        return self.__types

    @types.setter
    def types(self, value):
        self.__types = value
