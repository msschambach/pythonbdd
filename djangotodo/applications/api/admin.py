from django.contrib import admin
from .models import TodoList, TodoTask

admin.site.register(TodoList)
admin.site.register(TodoTask)
