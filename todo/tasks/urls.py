from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks-home'),
    path('tasks/', views.tasks_list, name='tasks-activity'),
    path('create/', views.task_create, name='task-create'),
    path('edit/<str:pk>/', views.edit, name='tasks-edit'),
    path('delete/<str:pk>/', views.task_delete, name='tasks-task-delete'),
]