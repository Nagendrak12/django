import django.forms as forms
from app.models import Movies_Series
from django.db import models

class MovieForm(forms.ModelForm):
    class Meta:
        model= Movies_Series
        fields ='__all__'


