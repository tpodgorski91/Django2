from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks-home'),
    path('tasks/', views.task, name='tasks-activity'),
    path('edit/', views.edit, name='tasks-edit'),
    path('delete/', views.task_delete, name='tasks-task-delete'),
]