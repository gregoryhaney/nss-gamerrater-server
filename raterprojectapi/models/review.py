from django.db import models


class Review(models.Model):
    review_body = models.CharField(max_length=150)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    