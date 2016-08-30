from django.contrib import admin
from core.models import Product, Entrance, ProductEntrance, Sale, ProductSale


admin.site.register(Product)

admin.site.register(Entrance)
admin.site.register(ProductEntrance)

admin.site.register(Sale)
admin.site.register(ProductSale)
