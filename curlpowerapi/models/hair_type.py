from django.db import models

class HairType(models.Model):
    hair_type = models.CharField(max_length=50)
