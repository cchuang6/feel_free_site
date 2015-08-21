from django.conf.urls import url, patterns

from dashBoard import views

urlpatterns = [url(r'^$', views.index, name='home'), ]

urlpatterns = patterns('',
                       url(r'^$', views.index, name='welcome'),
                       )
