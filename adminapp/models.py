from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=True,  blank=True)
    image_path = models.CharField(max_length=150, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return f'{self.pk}'


class Products(models.Model):
    name = models.CharField( max_length=150, null=False, blank=False)
    description = models.CharField(max_length=500, null=False,  blank=False)
    price = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=100, null=True)
    
    def get_url(self):
        return f'{self.pk}'
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    phone_number = models.CharField(null=False, unique=True, blank=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    payment_type = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=True, default=1)
    address = models.CharField(null=False, blank=False, max_length=250)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    count = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
