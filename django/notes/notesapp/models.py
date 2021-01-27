from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyNotes(models.Model):
    title=models.CharField(max_length=200)
    text_of_the_note=models.TextField(max_length=300)
    added_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}-{self.text_of_the_note}-{self.added_on}"

    
