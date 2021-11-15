from django.urls import path, include
from support.views import AnswerCreate, TaskViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'task', TaskViewSet)



urlpatterns = [

    path('', include(router.urls)),
    path ('create_answer/', AnswerCreate.as_view(), name = 'create_answer'),

]