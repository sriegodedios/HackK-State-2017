''' Handles Gets and Posts for history app '''

from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    ''' Sends a list of the worst hurricanes overall
    '''
    
    output = []
    for i in Hurricane.objects.order_by('max_wind')[:30]:
        output.append([i.start_date, i.name, i.max_wind, i.category])

    return render(request, 'history/base.html', {'table': output})