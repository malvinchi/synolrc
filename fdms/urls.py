#this is the url config module for fdms
from django.urls import path
from django.views.generic import TemplateView
from . import views
from  fdms.views import GreetingMsg


urlpatterns = [path("", views.fdms_home, name='welcome'),
               path("create/", views.fdms_create_mf, name="Create"),
               path("create/thanks/", views.fdms_thanks, name="ThankYou"),
               path("read/", TemplateView.as_view(template_name='fdms/read.html')),
               path("remove/", GreetingMsg.as_view()),
               path('update/', views.fdms_update, name='UpdateDB'),
               path('create/error/', views.fdms_error, name="error"),
               path('read_fm/', views.fdms_read, name='read'),
]
