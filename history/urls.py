from django.conf.urls import url
from django.shortcuts import render

from . import views

urlpatterns = [
    url(r'^$', views.generic, {'template_name': 'history/index.html'}, name='index'),
    url(r'^worst/$', views.worst, name='worst'),
    url(r'^worst/(?P<lat>\d+)/(?P<long>\d+)/(?P<radius>\d+)/$', views.worst),
    url(r'^map/$', views.generic, {'template_name': 'history/google_map_demo.html'}, name='map'),
    url(r'^training/$', views.generic, {'template_name': 'history/training.html'}, name='training'),
    url(r'^predict/$', views.predict, name='predict'),
]
