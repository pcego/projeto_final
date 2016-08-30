from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import Product, Entrance, ProductEntrance, Sale, ProductSale
from core.forms import ProductForm, EntranceForm, ProductEntranceForm, SaleForm, ProductSaleForm


def home(request):
    if request.user.is_authenticated():
        return redirect('url_core_board')
    return render(request, 'core/index.html')


@login_required()
def board(request):
    return render(request, 'core/board.html')


@login_required()
def products(request):
    data = {'product_list': Product.objects.all()}
    return render(request, 'core/products.html', data)


@login_required()
def product_update(request, id, template_name='core/product_form.html'):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('url_core_products')
    return render(request, template_name, {'form': form, 'product': product})


@login_required()
def product_create(request, template_name='core/product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_core_products')
    return render(request, template_name, {'form': form})


@login_required()
def product_delete(request, id, template_name='core/product_confirm_delete.html'):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('url_core_products')
    return render(request, template_name, {'object': product})


# Entrances views
@login_required()
def entrances(request):
    data = {'entrances_list': Entrance.objects.all()}
    return render(request, 'core/entrances.html', data)


@login_required()
def entrance_create(request, template_name='core/entrance_form_create.html'):
    form_entrance = EntranceForm(request.POST or None)

    if form_entrance.is_valid():
        entrance = form_entrance.save(commit=False)
        entrance.save()
        return redirect('url_core_entrance_product_insert', id=entrance.id)
    return render(request, template_name, {'form_entrance': form_entrance})


@login_required()
def entrance_update(request, id, template_name='core/entrance_form_create.html'):
    entrance = get_object_or_404(Entrance, id=id)
    form = EntranceForm(request.POST or None, instance=entrance)
    if form.is_valid():
        form.save()
        return redirect('url_core_entrance_product_insert', id=entrance.id)
    return render(request, template_name, {'form_entrance': form, 'entrance': entrance})


@login_required()
def entrance_product_insert(request, id):
    data = {}

    entrance = get_object_or_404(Entrance, id=id)
    data['entrance'] = entrance
    data['entrance_product_list'] = ProductEntrance.objects.filter(entrance=entrance)

    form_entrance = EntranceForm(instance=entrance)
    data['form_entrance'] = form_entrance

    form_product_entrance = ProductEntranceForm(request.POST or None)
    data['form_product_entrance'] = form_product_entrance

    if request.method == 'POST':
        if form_product_entrance.is_valid():
            product_entrance = form_product_entrance.save(commit=False)
            product_entrance.entrance = entrance
            product_entrance_insert_or_group(product_entrance)
            return redirect('url_core_entrance_product_insert', id=entrance.id)

    return render(request, 'core/entrance_form.html', data)


def product_entrance_insert_or_group(product_entrance):
    """This function will be used to group products in the Entrance
       If already there is this product in the Entrance List, it will increment the quantity and
       update the price
    """
    product = ProductEntrance.objects.filter(product=product_entrance.product, entrance=product_entrance.entrance)

    if product:
        product[0].quantity += product_entrance.quantity
        product[0].price = product_entrance.price
        product[0].save()
    else:
        product_entrance.save()


@login_required()
def entrance_product_delete(request, id):
    product_entrance = get_object_or_404(ProductEntrance, id=id)

    entrance_id = product_entrance.entrance.id

    product_entrance.delete()
    return redirect('url_core_entrance_product_insert', id=entrance_id)


@login_required()
def entrance_delete(request, id, template_name='core/entrance_confirm_delete.html'):
    entrance = get_object_or_404(Entrance, id=id)
    if request.method == 'POST':
        entrance.delete()
        return redirect('url_core_entrance')
    return render(request, template_name, {'object': entrance})


@login_required()
def sales(request):
    data = {'sales_list': Sale.objects.all()}
    return render(request, 'core/sales.html', data)


@login_required()
def sale_create(request, template_name='core/sale_form_create.html'):
    form_sale = SaleForm(request.POST or None)

    if form_sale.is_valid():
        sale = form_sale.save(commit=False)
        sale.save()
        return redirect('url_core_sale_product_insert', id=sale.id)
    return render(request, template_name, {'form_entrance': form_sale})


@login_required()
def sale_product_insert(request, id):
    data = {}

    sale = get_object_or_404(Sale, id=id)
    data['sale'] = sale
    data['sale_product_list'] = ProductSale.objects.filter(sale=sale)

    form_sale = SaleForm(instance=sale)
    data['form_sale'] = form_sale

    form_product_sale = ProductSaleForm(request.POST or None)
    data['form_product_sale'] = form_product_sale

    if request.method == 'POST':
        if form_product_sale.is_valid():
            product_sale = form_product_sale.save(commit=False)
            product_sale.sale = sale
            product_sale_insert_or_group(product_sale)
            return redirect('url_core_sale_product_insert', id=sale.id)

    return render(request, 'core/sale_form.html', data)


def product_sale_insert_or_group(product_sale):
    """
       This function will be used to group products in the Sale
       If already there is this product in the Sale List, it will increment the quantity
    """
    product = ProductSale.objects.filter(product=product_sale.product, sale=product_sale.sale)

    if product:
        product[0].quantity += product_sale.quantity
        product[0].save()
    else:
        product_sale.save()


@login_required()
def sale_update(request, id, template_name='core/sale_form_create.html'):
    sale = get_object_or_404(Sale, id=id)
    form = SaleForm(request.POST or None, instance=sale)
    if form.is_valid():
        form.save()
        return redirect('url_core_sale_product_insert', id=sale.id)
    return render(request, template_name, {'form_sale': form, 'sale': sale})


@login_required()
def sale_product_delete(request, id):
    product_sale = get_object_or_404(ProductSale, id=id)

    sale_id = product_sale.sale.id

    product_sale.delete()
    return redirect('url_core_sale_product_insert', id=sale_id)
