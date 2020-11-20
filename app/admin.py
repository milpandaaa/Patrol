from django.contrib import admin
from .models import *
models = [Person, Result]
admin.site.register(models)

# Register your models here.
