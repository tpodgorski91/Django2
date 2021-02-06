from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks-home'),
    path('tasks/', views.task, name='tasks-activity'),
    path('edit/<str:pk>/', views.edit, name='tasks-edit'),
    path('delete/<str:pk>/', views.task_delete, name='tasks-task-delete'),
]