
# Create your views here.
from django import template
from django.http  import HttpResponse
from django.shortcuts import render


def index(request):
    t = template.loader.get_template('beauasia/batemp/index.html')
    html = t.render()
    return HttpResponse(html)

def pgrs(request):
    t = template.loader.get_template('beauasia/batemp/pgrs.html')
    html = t.render()
    return HttpResponse(html)
