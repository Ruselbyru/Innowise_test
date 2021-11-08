from django.urls import path
from support.views import AnswerCreate, TaskList, TaskDetail, TaskUpdate


urlpatterns = [

    path ('task/', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task_detail'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path ('create_answer/', AnswerCreate.as_view(), name = 'create_answer'),

]