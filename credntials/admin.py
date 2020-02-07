from django.contrib import admin

# Register your models here.
from .models import InstType, Institutions, AccHolder, credntials

admin.site.register(credntials)
admin.site.register(AccHolder)

