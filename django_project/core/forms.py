from django.forms import ModelForm
from django_project.core.models import Product, Entrance, \
    ProductEntrance, Sale, ProductSale, Supplier

# cria um formulário a partir do modelo (tabela banco de dados)
# neste caso tabela produtos
class ProductForm(ModelForm):
    class Meta:
        model = Product
        # exibe no form os campos listados abaixo
        # caso queira que o campo nao seja exibido é só não adicionar a lista fields
        fields = ['bar_code', 'description', 'price', 'supplier']


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
        fields = ['sale_number', 'discount']


class ProductSaleForm(ModelForm):
    class Meta:
        model = ProductSale
        fields = ['product', 'quantity']


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name']
