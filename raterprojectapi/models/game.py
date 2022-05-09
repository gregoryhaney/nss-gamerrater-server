from django.db import models

class Game(models.Model):
    description = models.CharField(max_length=40)
    designer = models.CharField(max_length=20)
    number_of_players = models.IntegerField()
    time_to_play = models.IntegerField()
    age_rec = models.IntegerField()
    title = models.CharField(max_length=25)
    release_year = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category")