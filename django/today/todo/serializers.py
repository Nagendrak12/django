from rest_framework import serializers

from todo.models import Todo, UserTodo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('text', 'addedon')


class UserTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTodo
        fields = ('text', 'addedon')
