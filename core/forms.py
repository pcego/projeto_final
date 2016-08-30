from django.forms import ModelForm
from core.models import Product, Entrance, ProductEntrance, Sale, ProductSale


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['bar_code', 'description', 'price']


class EntranceForm(ModelForm):
    class Meta:
        model = Entrance
        fields = ['document_number', 'date']


class ProductEntranceForm(ModelForm):
    class Meta:
        model = ProductEntrance
        fields = ['product', 'quantity',  'price']


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['sale_number', 'date', 'discount']


class ProductSaleForm(ModelForm):
    class Meta:
        model = ProductSale
        fields = ['product', 'quantity']