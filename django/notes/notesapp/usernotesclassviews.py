from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from notesapp.models import MyNotes
from notesapp.serializers import MyNotesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class MyNotesList(generics.ListCreateAPIView):
    serializer_class = MyNotesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Get todos related current user
    def get_queryset(self):
        return MyNotes.objects.filter(user=self.request.user)

    # Set user to current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyNotesDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyNotesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MyNotes.objects.filter(user=self.request.user)
