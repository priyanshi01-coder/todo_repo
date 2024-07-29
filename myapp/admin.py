from django.contrib import admin

# Register your models here.

from .models import  Todo , Profile

admin.site.register(Todo)

admin.site.register(Profile)

