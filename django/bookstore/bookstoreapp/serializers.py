from rest_framework import serializers

from bookstoreapp.models import Book
# , UserTodo


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','price','number_of_pages','author','publisher')


# class UserTodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserTodo
#         fields = ('text', 'addedon')
