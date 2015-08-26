from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='home'),
                       url(r'^dashBoard2/', views.signUpTest, name='test'),
                       url(r'^thankyou/', views.thankyou),

                       )
