from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1024)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(max_length=1024, null=True, blank=True)
    

    def __str__(self):
        return self.name

class ProductComment(models.Model):
    """ Creates ProductComment table in database """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False,
                             related_name='comments')
    product_comment = models.TextField(null=False, blank=False,
                                    validators=[MaxLengthValidator(250)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date_added = models.DateField(
        auto_now_add=True, null=False, blank=False, editable=False
    )

    def __str__(self):
        return(self.product.name)
