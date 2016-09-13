from django.db import models
from django.db.models import Sum


class Supplier(models.Model):
    name = models.CharField('fornecedor', max_length=100)
    data_register = models.DateField('data cadastro', auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return self.name


class Product(models.Model):
    bar_code = models.CharField('código barras', max_length=100, unique=True)
    description = models.CharField('descrição', max_length=100)
    price = models.DecimalField('valor', max_digits=6, decimal_places=2, default=0)
    supplier = models.ForeignKey('Supplier', verbose_name='fornecedor')

    class Meta:
        ordering = ['description']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.description

    @property
    def stoq(self):
        entrances = ProductEntrance.objects.filter(product=self).aggregate(Sum('quantity'))
        sales = ProductSale.objects.filter(product=self).aggregate(Sum('quantity'))

        if entrances.get('quantity__sum')== None or sales.get('quantity__sum')== None:
            return 0

        return entrances.get('quantity__sum') - sales.get('quantity__sum')


class Entrance(models.Model):
    document_number = models.CharField('nf', max_length=20)
    date = models.DateField('data')

    class Meta:
        ordering = ['date']
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

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

    def entrances_per_month(month):
        product_entrances_list = ProductEntrance.objects.filter(entrance__date__month=month)

        amount = 0

        for product_entrance in product_entrances_list:
            amount += product_entrance.total
        return amount


class ProductEntrance(models.Model):
    quantity = models.IntegerField('quantidade')
    entrance = models.ForeignKey('Entrance', verbose_name='entrada')
    product = models.ForeignKey('Product', verbose_name='produto')
    price = models.DecimalField('valor', max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'entrada produto'
        verbose_name_plural = 'entrada produtos'

    def __str__(self):
        return self.product.description

    @property
    def total(self):
        return self.price * self.quantity


class Sale(models.Model):
    sale_number = models.CharField('venda', max_length=20)
    date = models.DateField('data venda')
    discount = models.DecimalField('desconto', max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['sale_number']
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

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

    def sales_per_month(month):
        sales_list = Sale.objects.filter(date__month=month)

        amount = 0

        for sale in sales_list:
            amount += sale.total

        return amount


class ProductSale(models.Model):
    product = models.ForeignKey('Product', verbose_name='produto')
    quantity = models.IntegerField('quantidade')
    sale = models.ForeignKey('Sale', verbose_name='venda')

    class Meta:
        verbose_name = 'item venda'
        verbose_name_plural = 'itens venda'

    def __str__(self):
        return self.product.description
