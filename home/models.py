from django.db import models

class Feature(models.Model):
    """
    Model to define the fields required to create
    features in the admin dashboard
    """
    header = models.CharField(max_length=254)
    text = models.TextField()
