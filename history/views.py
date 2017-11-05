''' Handles Gets and Posts for history app '''

from pandas import Series
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
import numpy

from .helpers import *

from django.shortcuts import render

from .models import *

# Create your views here.

def worst(request, lat=None, long=None, radius=None):
    ''' 
        Sends a list of the worst hurricanes overall
    '''
    print(lat, long, radius)
    if lat == None or long == None:
        header = ['Date', 'Name', 'Wind Speed', 'Category']
        output = []
        for i in Hurricane.objects.all().order_by('-max_wind')[:30]:
            temp_name = "N/A" if i.name == "UNNAMED" else i.name
            output.append([i.start_date.date(), temp_name, i.max_wind, i.category])
        return render(request, 'history/worst.html', {'table_head': header, 'table': output})
    

    return render(request, 'history/worst.html')

def predict(request):
    hurricanes_per_year = dict()
    for x in Hurricane.objects.filter(category__gte=1).order_by('start_date'):
        if x.start_date.year in hurricanes_per_year.keys():
            hurricanes_per_year[x.start_date.year] += 1
        else:
            hurricanes_per_year[x.start_date.year] = 1

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
    model_fit = model.fit(maxlag=50, disp=False)
    
    # predict with model
    predictions = model_fit.predict(start=len(data), end=len(data) + 10)
    for i, prediction in enumerate(predictions):
        x = prediction + last_ob
        years.append(last_year + i + 1)
        future_data.append(x)
        last_ob = x

    

    return render(request, 'history/graph.html', {'axis_labels': axis_labels, 'historic_data': historic_data, 'years': years, 'future_data': future_data})

def generic(request, template_name):
    return render(request, template_name)
