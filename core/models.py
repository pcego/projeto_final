from django.db import models


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


class ProductEntrance(models.Model):
    quantity = models.IntegerField()
    entrance = models.ForeignKey(Entrance)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.product.description
