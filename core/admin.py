from django.contrib import admin
from core.models import Product, Entrance, ProductEntrance, Sale, ProductSale, Supplier


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'bar_code', 'description', 'price', 'supplier', 'stoq')
    list_display_links = ('id', 'bar_code', 'description', 'price', 'supplier')
    list_filter = ('bar_code', 'description', 'supplier')
    search_fields = ('bar_code', 'description', 'supplier')

admin.site.register(Product, ProductAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'data_register')
    list_display_links = ('id', 'name', 'data_register')
    search_fields = ('id', 'name', 'data_register')
    list_filter = ('id', 'name', 'data_register')

admin.site.register(Supplier, SupplierAdmin)


class ProductEntranceInline(admin.TabularInline):
    """This will create a Master details in Admin Entrances"""
    model = ProductEntrance


class EntranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_number', 'date')
    list_display_links = ('id', 'document_number', 'date')
    list_filter = ('id', 'document_number', 'date')
    search_fields = ('id', 'document_number', 'date')

    inlines = [ProductEntranceInline,
               ]

admin.site.register(Entrance, EntranceAdmin)


class ProductSaleInline(admin.TabularInline):
    """This will create a Master details in Admin Sales"""
    model = ProductSale


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_number', 'date', 'discount')
    list_display_links = ('id', 'sale_number', 'date', 'discount')
    list_filter = ('sale_number', 'date')
    search_fields = ('id', 'sale_number', 'date', 'discount')

    inlines = [ProductSaleInline,
               ]
admin.site.register(Sale, SaleAdmin)


class ProductEntranceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'entrance', 'price', 'quantity')
    list_display_links = ('id', 'product', 'entrance', 'price', 'quantity')
    list_filter = ('product', 'entrance')
    search_fields = ('product', 'entrance', 'price')

admin.site.register(ProductEntrance, ProductEntranceAdmin)


class ProductSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'sale', 'quantity')
    list_display_links = ('id', 'product', 'sale', 'quantity')
    list_filter = ('product',)
    search_fields = ('product', 'sale')

admin.site.register(ProductSale, ProductSaleAdmin)
