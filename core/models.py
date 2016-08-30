from django.db import models
from django.db.models import Sum


class Product(models.Model):
    bar_code = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.description


class Entrance(models.Model):
    document_number = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.document_number

    @property
    def total(self):
        """This property will return the value amount of each entrance"""
        total_sum = 0
        entrance_products = ProductEntrance.objects.filter(entrance__id=self.id)
        for item in entrance_products:
            total_sum += item.price * item.quantity
        return total_sum


class ProductEntrance(models.Model):
    quantity = models.IntegerField()
    entrance = models.ForeignKey(Entrance)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.product.description


class Sale(models.Model):
    sale_number = models.CharField(max_length=20)
    date = models.DateField()
    discount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.sale_number

    @property
    def total(self):
        """This property will return the value amount of this sale"""
        total_sum = 0
        products = ProductSale.objects.filter(sale__id=self.id)
        for item in products:
            total_sum += item.product.price * item.quantity
        return total_sum


class ProductSale(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    sale = models.ForeignKey(Sale)
