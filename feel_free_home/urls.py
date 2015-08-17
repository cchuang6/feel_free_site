from django.conf.urls import url

from feel_free_home import views

urlpatterns = [url(r'^$', views.index, name='home'), ]
