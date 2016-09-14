from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy


urlpatterns = [

    # include de todas as urls da app core
    url(r'^', include('django_project.core.urls')),

    # url login padrão do admin do django
    url(r'^login/$', login,{"template_name": "core/login.html",},name="login"),


    # A view 'django.contrib.auth.views.logout' para /logout/URL.
    # é necessário passar três parâmetros sendo um deles um dicionário
    # informando qual página deve ser chamada após o logout.
    url(r'^logout/$', logout,{"next_page": reverse_lazy('url_core_home')}, name="logout"),

    # url admin do django
    url(r'^admin/', admin.site.urls),
]


admin.site.site_header = 'Estoque'
admin.site.index_title = 'Estoque'
admin.site.site_header = 'Sistema modelo de gestão de estoque'
admin.site.site_title = 'Sistema modelo de gestão de estoque'
