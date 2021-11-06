from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.http import HttpResponse



from .models import Task
from .serializers import (
    TaskSerializer,
    TaskCreateSerializer,
    TaskUpdateSerializer,
    TaskDetailSerializer,
    AnswerCreateSerializer,
)
# @api_view(['GET','POST'])
# def list_task(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response (serializer.data)
#
#     if request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201)
#         else:
#             return Response(status=400)

class TaskListAPIView (APIView):

    def get (self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response (serializer.data)


class TaskCreateAPIView (APIView):

    permission_classes = [permissions.IsAuthenticated]


    def post (self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response (status=404)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.id)




class TaskUpdateAPIView (APIView):

    permission_classes = [permissions.IsAdminUser]

    def put (self, request, id):
        try:
            task = Task.objects.get(pk=id)
        except Task.DoesNotExist:
            return HttpResponse (status=404)

        serializer = TaskUpdateSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response (status=404)


class TaskDetailAPIView (APIView):
    """Детали задания"""
    def get (self, request, id):
        task = Task.objects.get(pk=id)
        serializer = TaskDetailSerializer (task)
        return Response (serializer.data)


class AnswerCreateAPIView (APIView):
    """Добавление ответа"""
    permission_classes = [permissions.IsAuthenticated]

    def post (self, request):
        answer = AnswerCreateSerializer (data=request.data)
        if answer.is_valid():
            answer.save()
            return Response(answer.data)
        else:
            return Response(status=404)