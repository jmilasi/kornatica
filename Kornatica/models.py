from django.db import models


# Create your models here.
class Rooms(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)

