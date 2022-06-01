from pyexpat import model
from django.db import models
from rest_framework.views import APIView

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

