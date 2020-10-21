#this is the url config module for fdms
from django.urls import path
from . import views

urlpatterns = [path("", views.fdms_home, name='welcome'),
               path("create/", views.fdms_create_mf, name="Create"),
                path("create/thanks/", views.fdms_thanks, name="ThankYou"),
]
