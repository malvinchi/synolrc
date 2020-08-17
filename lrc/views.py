from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django import template
import datetime

# Create your views here.
def index(request):
    t = template.loader.get_template('lrc/homepage.html')
    html = t.render()
    return HttpResponse(html)

def index1(request):
    return HttpResponse("Welcome to Lrc 1")

def time_now(request):
    now=datetime.datetime.now()
    html ='<html><body> The time now is {0} </body></html>'.format(now)
    return HttpResponse(html)
