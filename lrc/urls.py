# this is the lrc appwide url config
from django.conf.urls import url
from lrc import views
from django.urls import path 

urlpatterns = [
    path('', views.index, name='home'),
    path('lrc1/', views.index1, name='home'),
    path('time/', views.time_now, name='time_now'),
]
