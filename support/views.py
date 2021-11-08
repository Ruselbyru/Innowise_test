from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import get_object_or_404

from support.models import Task, Answer
from support.serializers import TaskSerializer, TaskDetailSerializer, AnswerCreateSerializer, TaskUpdateSerializer
from support.permissions import IsOwnerOrReadOnly


class TaskViewSet (ModelViewSet):

    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def update(self, request, pk=None):
        queryset = Task.objects.get(pk=pk)
        serializer = TaskUpdateSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=400)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreate (CreateAPIView):
    """Answer create view"""
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
