from django.urls import path
from .views import AnswerCreate, TaskList, TaskDetail


urlpatterns = [

    path ('task/', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path ('create_answer/', AnswerCreate.as_view(), name = 'create_answer'),

]