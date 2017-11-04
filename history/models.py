from datetime import datetime
import pickle
import time

from django.db import models


# Create your models here.


class Hurricane(models.Model):

    name = models.CharField(max_length=10)

    def set_max_wind(self):
        # for x in HurricanePoint.objects.filter(parent=self).order_by('-wind'):
        #     print(x.wind, end=" ")
        # print()
        # print(HurricanePoint.objects.filter(parent=self).order_by('-wind')[0].wind)
        self.max_wind = HurricanePoint.objects.filter(parent=self).order_by('-wind')[0].wind

    def set_start_date(self):
        self.start_date = HurricanePoint.objects.filter(parent=self).order_by('-date')[0].date

    def set_category(self):
        wind = self.max_wind
        if wind >= 157:
            self.category = 5
        elif wind >= 130:
            self.category = 4
        elif wind >= 111:
            self.category = 3
        elif wind >= 96:
            self.category = 2
        elif wind >= 74:
            self.category = 1
        else:
            self.category = 0

    max_wind = models.IntegerField()

    start_date = models.DateTimeField()

    category = models.IntegerField()

    def __str__(self):
        return self.name
    
    @staticmethod
    def PrintAll():
        for x in Hurricane.objects.all().order_by("max_wind"):
            print(x.max_wind)

    @staticmethod
    def Update():
        
        for item in Hurricane.objects.all():
            #item.set_max_wind()
            #item.set_start_date()
            item.set_category()
            item.save()

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