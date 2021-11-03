from django.urls import path
from .views import TaskListView, TaskDetailView, AnswerCreateView, TaskCreateView

urlpatterns = [
    path('task/', TaskListView.as_view(), name = 'tasks'),
    path('task/<int:id>', TaskDetailView.as_view(), name = 'task'),
    path('answer/', AnswerCreateView.as_view(), name = 'answer'),
    path('create/', TaskCreateView.as_view(), name = 'create'),

]