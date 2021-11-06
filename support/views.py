from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Task, Answer
from .serializers import TaskSerializer, TaskDetailSerializer, AnswerCreateSerializer


class TaskList (ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetail (RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class AnswerCreate (CreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
