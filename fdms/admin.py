from django.contrib import admin

# Register your models here.
from .models import Institutions, Beneficary, Securities

admin.site.register(Institutions)
admin.site.register(Beneficary)
admin.site.register(Securities)
