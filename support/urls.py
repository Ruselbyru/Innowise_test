from django.urls import path, include
from support.views import AnswerCreate, TaskViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'task', TaskViewSet)


task_update = TaskViewSet.as_view({
    'put':'update',
})


urlpatterns = [

    path('', include(router.urls)),
    path ('task/<int:pk>/', task_update),
    path ('create_answer/', AnswerCreate.as_view(), name = 'create_answer'),

]