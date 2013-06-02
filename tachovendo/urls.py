from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
    url(r'^$', home, name="home"),
    url(r'^rain_info$', rain_info, name='rain_info'),
    url(r'^flood_info$', flood_info, name='flood_info'),
    url(r'^schools_info$', schools_info, name='schools_info'),
)
