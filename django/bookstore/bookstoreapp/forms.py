import django.forms as forms
from .models import Book,Publisher


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
