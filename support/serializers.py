from rest_framework import serializers
from .models import Task, Answer


class TaskListSerializer (serializers.ModelSerializer):
    """Список заданий"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    status = serializers.SlugRelatedField(slug_field='status_name', read_only=True)

    class Meta:
        model = Task
        fields = ('author', 'text', 'status')


class AnswerCreateSerializer (serializers.ModelSerializer):
    """Добавление ответа"""
    class Meta:
        model = Answer
        fields = ('task', 'author', 'text')


class RecursiveSerializer (serializers.Serializer):
    """Вывод рекурсивно только children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context = self.context)
        return serializer.data


class FilterAnswerListSerializer (serializers.ListSerializer):
    """Фильтр ответов - только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class AnswerSerializer (serializers.ModelSerializer):
    """Вывод ответа"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterAnswerListSerializer
        model = Answer
        fields = ('author', 'text', 'children')


class TaskDetailSerializer(serializers.ModelSerializer):
    """Детали задания"""
    status = serializers.SlugRelatedField(slug_field='status_name', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer (serializers.ModelSerializer):
    """Добавление ответа"""
    class Meta:
        model = Task
        fields = ('author', 'text')