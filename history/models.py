from datetime import datetime
import pickle
import time

from django.db import models


# Create your models here.


class Hurricane(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    # points = models.ManyToManyField("HurricanePoint")

    @staticmethod
    def Add(filename='C:\\Users\\Dylan Staatz\\Documents\\Documents\\Github\\HackK-State-2017\\data\\cleaned_data.pickle'):
        
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        
        start = time.time()
        count = 0
        for key in data:
            value = data[key]
            
            newHurricane = Hurricane.objects.create(name=value[0][0])

            newPoints = []
            for item in value:
                newPoints.append(HurricanePoint(
                    date=item[1], 
                    latitude=item[2], 
                    longitude=item[3], 
                    wind=item[4], 
                    parent=newHurricane,
                ))
            
            HurricanePoint.objects.bulk_create(newPoints)
            print(count, time.time() - start)
            count += 1


class HurricanePoint(models.Model):

    date = models.DateTimeField()

    latitude = models.FloatField()

    longitude = models.FloatField()

    wind = models.IntegerField()

    parent = models.ForeignKey("Hurricane", default=None)

    def __str__(self):
        return "DateTime: {0}, Lat: {1}, Long: {2}, Wind Speed: {3}".format(str(self.date), str(self.latitude), str(self.longitude), str(self.wind))