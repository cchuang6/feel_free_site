from visualization import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', views.index, name='visualization'),
                       )