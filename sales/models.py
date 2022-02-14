from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
from customers.models import Customer
from products.models import Product
from profiles.models import Profile
from .utils import generate_code


class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def get_sales_id(self):
        sales_obj = self.sales_set.first()
        return sales_obj.id

    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"

    class Meta:
        verbose_name = 'position'
        verbose_name_plural = 'positions'


class Sales(models.Model):
    transaction_id = models.CharField(max_length=25, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sales_man = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sales for amount of ${self.total_price}"

    def get_absolute_url(self):
        return reverse('sales:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    class Meta:
        verbose_name = 'sale'
        verbose_name_plural = 'sales'


class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)

    class Meta:
        verbose_name = 'csv'
        verbose_name_plural = 'csvs'





