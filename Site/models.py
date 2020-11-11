from django.db import models
from django.shortcuts import reverse
import os

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

    main_image = models.ImageField(
        upload_to='images'
    )
    gallery1 = models.ImageField(
        upload_to='images'
    )
    gallery2 = models.ImageField(
        upload_to='images'
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
    metric_num = models.CharField(
        max_length=6,
        default='кг.'
    )
    old_price = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    promo_price = models.DecimalField(
        decimal_places=2,
        max_digits=7,
        blank=True,
        null=True
    )
    available_qty = models.DecimalField(
        decimal_places=2,
        max_digits=7
    )
    attach_file = models.FileField(
        upload_to='attached_files',
        blank=True,
        null=True
    )

    def filename(self):
        return os.path.basename(self.attach_file.name)
    
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

    def __str__(self):
        return self.name

    def get_promo_percent(self):
        return round((
            self.old_price - self.promo_price
            ) / self.old_price * 100)

    def get_weight(self):
        return f'{str(self.weight)} {self.metric_num}'

    def get_absolute_url(self):
        return reverse('pytek:details', kwargs={
            'slug':self.slug
        })
