from django.urls import path
from .views import (
    TaskListAPIView,
    TaskCreateAPIView,
    TaskUpdateAPIView,
    TaskDetailAPIView,
    AnswerCreateAPIView,
)

urlpatterns = [

    path ('task/', TaskListAPIView.as_view(), name='task_list'),
    path('task/<int:id>/', TaskDetailAPIView.as_view(), name = 'task'),
    path ('create_task/', TaskCreateAPIView.as_view(), name='create_task'),
    path ('update_task/<int:id>/', TaskUpdateAPIView.as_view(), name='update_task'),
    path ('create_answer/', AnswerCreateAPIView.as_view(), name = 'create_answer'),

]