from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
  list_display = ("title", "description", "completed")

# Register models

admin.site.register(Tasks, TasksAdmin)
