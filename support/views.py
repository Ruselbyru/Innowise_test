from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import Task, Answer
from .serializers import TaskListSerializer, TaskDetailSerializer, AnswerCreateSerializer, TaskCreateSerializer


class TaskListView (APIView):
    """Список заданий"""
    def get (self, request):
        tasks = Task.objects.all()
        serializer = TaskListSerializer (tasks, many=True)
        return Response (serializer.data)


class TaskDetailView (APIView):
    """Детали задания"""
    def get (self, request, id):
        task = Task.objects.get(pk=id)
        serializer = TaskDetailSerializer (task)
        return Response (serializer.data)


class AnswerCreateView (APIView):
    """Добавление ответа"""
    def post (self, request):
        answer = AnswerCreateSerializer (data=request.data)
        if answer.is_valid():
            answer.save()
        return Response(status=201)


class TaskCreateView (APIView):
    """Добавление задания"""
    def post (self, request):
        task = TaskCreateSerializer (data=request.data)
        if task.is_valid():
            task.save()
            return Response(status=201)
        else:
            return Response(status=404)
