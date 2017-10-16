from rest_framework import serializers
from applications.api.models import TodoList, TodoTask


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'name', 'description', 'created', 'modified')


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = ('id', 'name', 'description', 'due_date', 'created', 'modified')
