from django.contrib import admin
from .models import TaskList  # if you want to import from the specific appname jst replace .models with appname.models
# Register your models here.

admin.site.register(TaskList)
