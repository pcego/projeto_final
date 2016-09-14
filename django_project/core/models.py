from django.db import models
from django.db.models import Sum

# classe Supplier herda de models.Model
# nesta classe você declara os campos da sua tabela de banco
# e o tipo de cada campo, tamanho e parâmetros adicionais
# o ORM do django irá se encarregar de ler e criar a tabela
# com seus devidos campos no seu banco de dados
class Supplier(models.Model):

    # cria um campo name na tabela supplier
    # com tamanho máximo igual a 100 e do tipo varchar
    name = models.CharField('fornecedor', max_length=100)

    # cria um campos data_register do tipo date
    # e carrega o campo por default com a data atual
    data_register = models.DateField('data cadastro', auto_now_add=True)

    class Meta:

        # utilizado pelo admin do django para ordenar
        # os fornecedores pelo nome
        ordering = ['name']
        # utilizado pelo admin do django
        # para nomear o campo com um nome escolhdo por você
        verbose_name = 'fornecedor'
        # nome no plural a ser utilizado pelo admin
        verbose_name_plural = 'fornecedores'

    # retorna o valor do campo name (utilizado pelo admin)
    def __str__(self):
        return self.name

# classe para criar a tabela products no bd
class Product(models.Model):
    # cria campo do tipo varchar, com tamanho 100, e único
    # ou seja não é possível cadastrar dois códigos iguais
    bar_code = models.CharField('código barras', max_length=100, unique=True)
    description = models.CharField('descrição', max_length=100)
    # cria um campo do tipo decimal, maximo de digitos 6
    # duas casas decimais e por padrão seu valor será zero
    price = models.DecimalField('valor', max_digits=6, decimal_places=2, default=0)

    # cria uma chave estrangeira na tabela products
    # significa uma relação 1-n ou seja um forncedor possui vários produtos
    # mas um produto foi fornecido por um forncedor específico
    supplier = models.ForeignKey('Supplier', verbose_name='fornecedor')

    class Meta:
        ordering = ['description']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.description

    @property
    # Método para cálculo do estoque disponível
    def stoq(self):

        # realiza uma query no banco de dados na tabela product_entrance
        # e filtrando pelo produto, agregando e somando as quantidades
        entrances = ProductEntrance.objects.filter(product=self).aggregate(Sum('quantity'))

        # realiza a mesma query acima mas na tabela sales (vendas)
        sales = ProductSale.objects.filter(product=self).aggregate(Sum('quantity'))

        # condição para verificar se há entrada de um produto ou a venda do mesmo
        # caso não haja retorna o valor do estoque igual a zero
        if entrances.get('quantity__sum')== None or sales.get('quantity__sum')== None:
            return 0

        # retorna o estoque atual do produto solicitado
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
    date = models.DateField('data venda', auto_now_add=True)
    discount = models.DecimalField('desconto', max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['sale_number']
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __str__(self):
        return self.sale_number

    @property
    # método para calcular valor total da venda
    # considerando o desconto
    def total(self):

        total_sum = 0
        products = ProductSale.objects.filter(sale__id=self.id)
        for item in products:
            total_sum += (item.product.price * item.quantity) - self.discount
        return total_sum

    # método para calcular o valor mensal das vendas
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
