from __future__ import unicode_literals

from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()


class TodoTask(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=280)
    due_date = models.DateTimeField(auto_now=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()
