from django.db import models
from .product import Product
from .hair_type import HairType

class ProductHairType(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    hair_type = models.ForeignKey(HairType, on_delete = models.CASCADE)
