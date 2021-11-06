from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView,UpdateAPIView

from .models import Task, Answer
from .serializers import TaskSerializer, TaskDetailSerializer, AnswerCreateSerializer, TaskUpdateSerializer


class TaskList (ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TaskDetail (RetrieveAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskUpdate (UpdateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


class AnswerCreate (CreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
