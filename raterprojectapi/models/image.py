from django.db import models

class Image(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
