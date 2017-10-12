from rest_framework import viewsets
from . import models, serializers


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodoListSerializer
    queryset = models.TodoList.objects.all()


class TodoTaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodoTaskSerializer
    queryset = models.TodoTask.objects.all()
