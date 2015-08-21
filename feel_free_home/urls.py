from django.conf.urls import url, patterns
from solid import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='home'),
                       )