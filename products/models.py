from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text='in US dollars $')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
