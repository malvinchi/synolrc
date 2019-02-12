from django.urls import path
from beauasia import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pgrs/', views.pgrs, name = 'pgres'),
]
