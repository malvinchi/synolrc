from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from credntials import views

urlpatterns = [
    path('', views.index, name='chome'),
]
