from django.db import models

# Create your models here.
class Movies_Series(models.Model):
    name_of_series=models.CharField(max_length=100)
    director_name=models.CharField(max_length=50)
    movie_link=models.CharField(max_length=300)
    number_of_episodes=models.IntegerField()
    
    def __str__(self):
        return f"{self.id}-{self.name_of_series}-{self.director_name}-{self.movie_link}-{self.number_of_episodes}"
    
