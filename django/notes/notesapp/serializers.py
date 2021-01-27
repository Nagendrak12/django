from rest_framework import serializers

from notesapp.models import MyNotes


class MyNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNotes
        fields = ('title', 'text_of_the_note')

