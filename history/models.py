from datetime import datetime
import pickle

from django.db import models


# Create your models here.


class Hurricane(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    # points = models.ManyToManyField("HurricanePoint")

    @staticmethod
    def MassAddFromFile(filename='C:\\Users\\Dylan Staatz\\Documents\\Documents\\Github\\HackK-State-2017\\data\\cleaned_data.pickle'):
        
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        
        for key in data:
            value = data[key]
            newHurricane = Hurricane.objects.create(name=value[0][0])
            newPoints = []
            for item in value:
                HurricanePoint.objects.create(
                    date=item[1], 
                    latitude=item[2], 
                    longitude=item[3], 
                    wind=item[4], 
                    parent=newHurricane,
                )
            break


class HurricanePoint(models.Model):

    date = models.DateTimeField()

    latitude = models.FloatField()

    longitude = models.FloatField()

    wind = models.IntegerField()

    parent = models.ForeignKey("Hurricane")

    def __str__(self):
        return 