from rest_framework import routers
from applications.api.views import TodoListViewSet, TodoTaskViewSet

router = routers.SimpleRouter()
router.register(r'lists', TodoListViewSet)
router.register(r'tasks', TodoTaskViewSet)

urlpatterns = router.urls
