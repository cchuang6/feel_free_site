from django.conf.urls import url, patterns

from . import views

# urlpatterns = [url(r'^$', views.index, name='home'), ]

urlpatterns = [url(r'^$', views.welcome, name='dashBoard-welcome'),]


