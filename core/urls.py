from django.conf.urls import url
from core.views import home, board, entrances, products, product_update, product_create, product_delete, entrance_create, \
    entrance_product_insert, entrance_delete, entrance_update, entrance_product_delete, sales, sale_create, \
    sale_product_insert, sale_update, sale_product_delete, reports, supplier, supplier_create, supplier_delete, \
    supplier_update

urlpatterns = [
    url(r'^$', home, name='url_core_home'),
    url(r'^board/$', board, name='url_core_board'),

    # Product URL's
    url(r'^products/$', products, name='url_core_products'),
    url(r'^product-create/$', product_create, name='url_core_products_create'),
    url(r'^product-update/(?P<id>\d+)$', product_update, name='url_core_product_update'),
    url(r'^product-delete/(?P<id>\d+)$', product_delete, name='url_core_product_delete'),

    # Supplier URL's
    url(r'^supplier/$', supplier, name='url_core_supplier'),
    url(r'^supplier-create/$', supplier_create, name='url_core_supplier_create'),
    url(r'^supplier-update/(?P<id>\d+)$', supplier_update, name='url_core_supplier_update'),
    url(r'^supplier-delete/(?P<id>\d+)$', supplier_delete, name='url_core_supplier_delete'),

    # Entrances URL's
    url(r'^entrances/$', entrances, name='url_core_entrance'),
    url(r'^entrance-create/$', entrance_create, name='url_core_entrance_create'),
    url(r'^entrance-update/(?P<id>\d+)$', entrance_update, name='url_core_entrance_update'),
    url(r'^entrance-delete/(?P<id>\d+)$', entrance_delete, name='url_core_entrance_delete'),
    url(r'^entrance-product-insert/(?P<id>\d+)$', entrance_product_insert, name='url_core_entrance_product_insert'),
    url(r'^entrance-product-delete/(?P<id>\d+)$', entrance_product_delete, name='url_core_entrance_product_delete'),

    # Sales URL's
    url(r'^sales/$', sales, name='url_core_sales'),
    url(r'^sale-create/$', sale_create, name='url_core_sale_create'),
    url(r'^sale-update/(?P<id>\d+)$', sale_update, name='url_core_sale_update'),
    url(r'^sale-product-insert/(?P<id>\d+)$', sale_product_insert, name='url_core_sale_product_insert'),
    url(r'^sale-product-delete/(?P<id>\d+)$', sale_product_delete, name='url_core_sale_product_delete'),

    # Reports URL's
    url(r'^reports/$', reports, name='url_core_reports')
]
