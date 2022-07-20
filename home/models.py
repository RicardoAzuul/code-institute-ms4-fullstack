from django.db import models

class Feature(models.Model):
    header = models.CharField(max_length=254)
    text = models.TextField()
