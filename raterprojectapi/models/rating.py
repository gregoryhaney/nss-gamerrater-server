from django.db import models

class Rating(models.Model):
    rating = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
   