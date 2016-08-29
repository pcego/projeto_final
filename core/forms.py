from django.forms import ModelForm
from core.models import Product, Entrance, ProductEntrance


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
        fields = ['quantity', 'product']
