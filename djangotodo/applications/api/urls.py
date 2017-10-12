from django.conf.urls import url
from rest_framework import routers
from .views import TodoListViewSet, TodoTaskViewSet

router = routers.SimpleRouter()
router.register(r'lists', TodoListViewSet)
router.register(r'tasks', TodoTaskViewSet)

urlpatterns = router.urls
