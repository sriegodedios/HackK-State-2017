''' Handles Gets and Posts for history app '''
from operator import attrgetter

from pandas import Series
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import numpy

from .helpers import *

from django.shortcuts import render

from .models import *

# Create your views here.

def history(request, lat=None, long=None):
    ''' 
        Sends a list of the worst hurricanes overall
    '''
    header = ['', 'Date', 'Name', 'Wind Speed', 'Category']

    if lat == None or long == None:
        output = []
        for i, x in enumerate(Hurricane.objects.all().order_by('-max_wind')[:100]):
            temp_name = "N/A" if x.name == "UNNAMED" else x.name
            output.append([i+1, x.start_date.date(), temp_name, x.max_wind, x.category])
        return render(request, 'history/historical.html', {'table_head': header, 'table': output})

    radius = 1.75
    newlat = float(lat)
    newlong = float(long) * -1
    print(newlat, newlong)
    hurricanes = []

    for point in HurricanePoint.objects.filter(
            latitude__gte=newlat-radius, 
            latitude__lte=newlat+radius, 
            longitude__gte=newlong-radius, 
            longitude__lte=newlong+radius
            ):
        if point.parent not in hurricanes:
            hurricanes.append(point.parent)
    output = []
    newHurricanes = sorted(hurricanes, key=attrgetter('max_wind'), reverse=True)
    
    for i, x in enumerate(newHurricanes):
        temp_name = "N/A" if x.name == "UNNAMED" else x.name
        output.append([i+1, x.start_date.date(), temp_name, x.max_wind, x.category])

    return render(request, 'history/historical.html', {'table_head': header, 'table': output})

def predict(request, lat=None, long=None):

    hurricanes_per_year = dict()
    if lat == None or long == None:
        for x in Hurricane.objects.filter(category__gte=0).order_by('start_date'):
            if x.start_date.year in hurricanes_per_year.keys():
                hurricanes_per_year[x.start_date.year] += 1
            else:
                hurricanes_per_year[x.start_date.year] = 1
    else:
        radius = 1.75
        newlat = float(lat)
        newlong = float(long) * -1
        print(newlat, newlong)
        hurricanes = []

        for point in HurricanePoint.objects.filter(
                latitude__gte=newlat-radius, 
                latitude__lte=newlat+radius, 
                longitude__gte=newlong-radius, 
                longitude__lte=newlong+radius
                ):
            if point.parent not in hurricanes:
                hurricanes.append(point.parent)
        for i in range(1851, 2015):
            hurricanes_per_year[i] = 0
        for x in sorted(hurricanes, key=attrgetter('start_date')):
            if x.start_date.year in hurricanes_per_year.keys():
                hurricanes_per_year[x.start_date.year] += 1
            else:
                hurricanes_per_year[x.start_date.year] = 1
    
    isNull = False

    axis_labels = ["Year", "Frequency"]
    years = []
    historic_data = []
    future_data = []
    for key in hurricanes_per_year.keys():
        years.append(key)
        historic_data.append(hurricanes_per_year[key])
        future_data.append(0)

    # load dataset
    series = Series(hurricanes_per_year)
    last_ob = series.values[-1]
    last_year = series.keys()[-1]

    #difference dataset
    data = difference(series.values)

    # fit model
    model = AR(data)
    model_fit = model.fit(maxlag=5, disp=False)
    
    # predict with model
    predictions = model_fit.predict(start=len(data), end=len(data) + 10)
    for i, prediction in enumerate(predictions):
        x = prediction + last_ob
        years.append(last_year + i + 1)
        future_data.append(x)
        last_ob = x

    return render(request, 'history/predict.html', {'axis_labels': axis_labels, 'historic_data': historic_data, 'years': years, 'future_data': future_data, 'null': isNull})

def generic(request, template_name):
    return render(request, template_name)
