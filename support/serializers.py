from rest_framework import serializers

from .models import Task, Answer, Status


class TaskSerializer (serializers.ModelSerializer):
    "Задание"
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    status = serializers.SlugRelatedField(slug_field='status_name', read_only=True)

    class Meta:

        model = Task
        fields = '__all__'


class TaskUpdateSerializer (serializers.ModelSerializer):

    status = serializers.SlugRelatedField(slug_field='status_name', queryset=Status.objects.all())

    class Meta:

        model = Task
        fields = ['status']


class AnswerCreateSerializer (serializers.ModelSerializer):
    """Добавление ответа"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    task = serializers.SlugRelatedField(slug_field='id', queryset=Task.objects.all())
    parent = serializers.SlugRelatedField(slug_field='id',
                                          queryset= Answer.objects.all(),
                                          allow_null=True, default= None)

    class Meta:

        model = Answer
        fields = '__all__'


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
    children = RecursiveSerializer(many=True,read_only=True)

    class Meta:

        list_serializer_class = FilterAnswerListSerializer
        model = Answer
        fields = ('id', 'author', 'text', 'children')


class TaskDetailSerializer(serializers.ModelSerializer):
    """Детали задания"""
    status = serializers.SlugRelatedField(slug_field='status_name', queryset=Status.objects.all())
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    answer = AnswerSerializer(many=True,read_only=True)

    class Meta:

        model = Task
        fields = '__all__'