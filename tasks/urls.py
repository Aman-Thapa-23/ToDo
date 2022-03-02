from unicodedata import name
from django.urls import path
from .views import TasksListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name= 'tasks'

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),

]