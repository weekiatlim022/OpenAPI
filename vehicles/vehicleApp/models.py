from django.db import models

# Create your models here.
class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    passenger = models.IntegerField(default=0)
