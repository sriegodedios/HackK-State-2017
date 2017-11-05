''' Handles Gets and Posts for history app '''

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

    header = ["Year", "Frequency"]
    years = []
    data = []
    for key in hurricanes_per_year.keys():
        years.append(key)
        data.append(hurricanes_per_year[key])


    return render(request, 'history/graph.html', {'table_head': header, 'years': years, 'data': data})

def generic(request, template_name):
    return render(request, template_name)
