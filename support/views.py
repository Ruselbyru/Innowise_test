from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView,UpdateAPIView

from support.models import Task, Answer
from support.serializers import TaskSerializer, TaskDetailSerializer, AnswerCreateSerializer, TaskUpdateSerializer


class TaskList (ListCreateAPIView):
    """Task list or create task view"""
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetail (RetrieveAPIView):
    """Task detail view"""
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskUpdate (UpdateAPIView):
    """Task update view"""
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


class AnswerCreate (CreateAPIView):
    """Answer create view"""
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
