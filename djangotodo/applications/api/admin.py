from django.contrib import admin
from applications.api.models import TodoList, TodoTask

admin.site.register(TodoList)
admin.site.register(TodoTask)
