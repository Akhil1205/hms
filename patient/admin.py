from django.contrib import admin

# Register your models here.
from .models import patient,visited_time
admin.site.register(patient)
admin.site.register(visited_time)