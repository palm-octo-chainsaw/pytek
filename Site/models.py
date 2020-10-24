from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    #parent = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField()

class Product(models.Model):
    name = models.CharField(
        max_length=255
    )
    slug = models.SlugField()
    main_image = models.CharField(
        max_length=255
    )
    gallery = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )
    number = models.CharField(
        max_length=6
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    # metric_num = models.ForeignKey(
    #     Category, 
    #     on_delete=models.CASCADE
    # )
    old_price = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    promo_price = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    available_qty = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    #attach_file = 
    specifications = models.CharField(
        max_length=255
    )
    new_product = models.BooleanField()
    video = models.CharField(
        max_length=255
    )
    weight = models.DecimalField(
        decimal_places=2,
        max_digits=5
    )
    #connected_products = 
    #bought_together = 
    meta_description = models.CharField(
        max_length=255
    )
    meta_keywords = models.CharField(
        max_length=255
    )
    meta_title = models.CharField(
        max_length=255
    )
    active = models.BooleanField()