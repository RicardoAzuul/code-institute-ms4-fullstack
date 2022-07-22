from django.db import models


class Product_Category(models.Model):
    """
    Model to define the fields required to create product categories
    """

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
    """
    Model to define the fields required to create products
    """
    category = models.ForeignKey(
        'Product_Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class ShopAlert(models.Model):
    """
    Model to define the fields required to create shop alerts
    """
    name = models.CharField(max_length=254)
    text = models.TextField()
