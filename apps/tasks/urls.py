from django.urls import path


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = router.urls

from apps.tasks.views import GetTasksView, CreateTaskView

urlpatterns += [
    path('tasks/', GetTasksView.as_view(), name = 'task_list'),
    path('tasks/create', CreateTaskView().as_view(), name = 'task_create')
]
