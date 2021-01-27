import django.forms as forms
from .models import MyNotes


class MyNotesForm(forms.ModelForm):
    class Meta:
        model = MyNotes
        fields = ['title','text_of_the_note']


class MyNotesEditForm(forms.ModelForm):
    class Meta:
        model = MyNotes
        fields = ['title', 'text_of_the_note']
