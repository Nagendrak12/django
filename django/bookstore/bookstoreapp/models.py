from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    website = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    number_of_pages = models.IntegerField()
    author = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}-{self.title}-{self.author}-{self.publisher}-{self.number_of_pages}-{self.publisher.id}"
