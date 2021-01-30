from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks-home'),
    path('tasks/', views.task, name='tasks-activity'),
]