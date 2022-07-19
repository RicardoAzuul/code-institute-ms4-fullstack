from django.db import models

# Create your models here.
# TODO: use models.py in products as basis
class BodyPart(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def friendly_name2(self):
        return self.friendly_name


class Equipment(models.Model):
    # Equipment has no plural, so we have to set the plural
    class Meta:
        verbose_name_plural = 'Equipment'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def friendly_name2(self):
        return self.friendly_name


class Target(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def friendly_name2(self):
        return self.friendly_name


class Workout(models.Model):
    # TODO: Change body_part to bodypart
    body_part = models.ForeignKey(
        'BodyPart', null=True, blank=True, on_delete=models.SET_NULL)
    equipment = models.ForeignKey(
        'Equipment', null=True, blank=True, on_delete=models.SET_NULL)
    target = models.ForeignKey(
        'Target', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
