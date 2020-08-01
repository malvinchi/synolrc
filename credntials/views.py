## Crednetial app views

from django.shortcuts import render
from django.http import HttpResponse
from credntials import views
from django import template

# Create your views here.

def index(request):
    t1 = template.loader.get_template('credntials/index.html')
    html = t1.render()
    return HttpResponse(html)
