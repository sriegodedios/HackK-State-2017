from django.conf.urls import url
from django.shortcuts import render

from . import views

urlpatterns = [
    url(r'^$', views.generic, {'template_name': 'history/index.html'}, name='index'),
    url(r'^worst/', views.worst, name='worst'),
    url(r'^worst/(?P<lat>\d+\.\d+)/(?P<long>\d+\.\d+)/$', views.worst),
    url(r'^map_demo/', views.generic, {'template_name': 'history/google_map_demo.html'}, name='map_demo'),
    url(r'^training/', views.generic, {'template_name': 'history/training.html'}, name='training'),
    url(r'^predict', views.predict, name='predict'),
]
