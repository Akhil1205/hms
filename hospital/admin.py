from django.contrib import admin

# Register your models here.
from .models import hospital,department
admin.site.register(hospital)
admin.site.register(department)