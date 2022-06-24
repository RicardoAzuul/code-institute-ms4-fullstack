from tabnanny import verbose
from django.db import models

# Create your models here.
class Product_Category(models.Model):

    class Meta:
        verbose_name_plural = 'Product_Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def friendly_name2(self):
        return self.friendly_name


class Product(models.Model):
    # on_delete=models.SET_NULL means that products using the category will have the category value deleted when the category itself is deleted
    category = models.ForeignKey('Product_Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
