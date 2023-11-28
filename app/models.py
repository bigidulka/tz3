from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(item.price for item in self.items.all())

class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount_percentage = models.FloatField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def is_valid(self):
        now = timezone.now()
        return self.valid_from <= now <= self.valid_to

class Tax(models.Model):
    name = models.CharField(max_length=100)
    tax_percentage = models.FloatField()