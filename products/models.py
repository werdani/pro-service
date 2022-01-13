from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    seller = models.CharField(max_length=55)
    price = models.FloatField()

    def __str__(self):
        return f"{self.id}.{self.name}"
