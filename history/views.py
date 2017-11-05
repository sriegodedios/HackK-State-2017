''' Handles Gets and Posts for history app '''

from pandas import Series
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import numpy

from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    ''' Sends a list of the worst hurricanes overall
    '''
    header = ['Date', 'Name', 'Wind Speed', 'Category']
    output = []
    for i in Hurricane.objects.all().order_by('-max_wind')[:30]:
        temp_name = "N/A" if i.name == "UNNAMED" else i.name
        output.append([i.start_date.date(), temp_name, i.max_wind, i.category])

    return render(request, 'history/index.html', {'table_head': header, 'table': output})

def per_year(request):
    hurricanes_per_year = dict()
    for x in Hurricane.objects.filter(max_wind__gte=50).order_by('start_date'):
        if x.start_date.year in hurricanes_per_year.keys():
            hurricanes_per_year[x.start_date.year] += 1
        else:
            hurricanes_per_year[x.start_date.year] = 1
<<<<<<< HEAD
    
    series = Series(data=hurricanes_per_year)


=======

    header = ["Year", "Frequency"]
>>>>>>> Shane
    years = []
    data = []
    for key in hurricanes_per_year.keys():
        years.append(key)
        data.append(hurricanes_per_year[key])

<<<<<<< HEAD
    return render(request, 'history/index.html', {'years': years, 'data': data})
=======

    return render(request, 'history/graph.html', {'table_head': header, 'years': years, 'data': data})
>>>>>>> Shane

def generic(request, template_name):
    return render(request, template_name)
