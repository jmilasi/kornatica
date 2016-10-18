from django.db import models


# Create your models here.
class Language(models.Model):
    Name = models.CharField(max_length=100)
    Abbr = models.CharField(max_length=10)


class InstanceType(models.Model):
    Name = models.CharField(max_length=100)


class Translation(models.Model):
    Value = models.CharField(max_length=1000)
    Type = models.ForeignKey(InstanceType, on_delete=models.CASCADE)
    LanguageId = models.ForeignKey(Language, on_delete=models.CASCADE)


class Rooms(models.Model):
    NameTranslationId = models.ForeignKey(Translation, default=0, null=False, on_delete=models.CASCADE, related_name='Name')
    DescriptionTranslationId = models.ForeignKey(Translation, default=0, null=False, on_delete=models.CASCADE, related_name='Description')
    #LocationX = models.CharField(max_length=100)
    #LocationY = models.CharField(max_length=100)
    DistanceFromSee = models.IntegerField(default=0)
    DistanceFromCenter = models.IntegerField(default=0)
    NumberOfSeats = models.IntegerField(default=0, null=False)
    Pets = models.BooleanField(default=0, null=False)
    Parking = models.BooleanField(default=0, null=False)
    TV = models.BooleanField(default=0, null=False)
    Satellite = models.BooleanField(default=0, null=False)
    WiFi = models.BooleanField(default=0, null=False)




