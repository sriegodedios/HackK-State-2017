from django.conf.urls import url
from django.shortcuts import render

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'map_demo/', views.generic, {'template_name': 'history/google_map_demo.html'}, name='map_demo'),
    url(r'^per_year', views.per_year, name='per_year'),
]
