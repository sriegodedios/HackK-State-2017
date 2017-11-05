from django.conf.urls import url
from django.shortcuts import render

from . import views

urlpatterns = [
    url(r'^$', views.generic, {'template_name': 'history/index.html'}, name='index'),
    url(r'^history/$', views.history, name='history'),
    url(r'^about-us/$', views.generic, {'template_name': 'history/about-us.html'}, name='about-us'),
    url(r'^history/(?P<lat>.+)/(?P<long>.+)/$', views.history),
    url(r'^map/$', views.generic, {'template_name': 'history/google_map_demo.html'}, name='map'),
    url(r'^training/$', views.generic, {'template_name': 'history/training.html'}, name='training'),
    url(r'^predict/$', views.predict, name='predict'), 
    url(r'^predict/(?P<lat>.+)/(?P<long>.+)/$', views.predict, name='predict'),
]
