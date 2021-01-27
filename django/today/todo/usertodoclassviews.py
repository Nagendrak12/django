from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication

from todo.models import UserTodo
from todo.serializers import UserTodoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class UserTodoList(generics.ListCreateAPIView):
    serializer_class = UserTodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Get todos related current user
    def get_queryset(self):
        return UserTodo.objects.filter(user=self.request.user)

    # Set user to current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
