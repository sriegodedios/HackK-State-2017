''' Handles Gets and Posts for history app '''

from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    ''' Sends a list of the worst hurricanes overall
    '''
    header = ['Date', 'Name', 'Wind Speed', 'Category']
    output = []
    for i in Hurricane.objects.order_by('-max_wind')[:30]:
        output.append([i.start_date, i.name, i.max_wind, i.category])

    return render(request, 'history/index.html', {'table_head': header, 'table': output})

def generic(request, template_name):
    return render(request, template_name)