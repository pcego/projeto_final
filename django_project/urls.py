"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    url(r'^', include('django_project.core.urls')),
    url(r'^login/$', login,{"template_name": "core/login.html",},name="login"),

    # Map the 'django.contrib.auth.views.logout' view to the /logout/ URL.
    # Pass additional parameters to the view like the page to show after logout
    # via a dictionary used as the 3rd argument.
    url(r'^logout/$', logout,{"next_page": reverse_lazy('url_core_home')}, name="logout"),
    url(r'^admin/', admin.site.urls),
]


admin.site.site_header = 'Estoque'
admin.site.index_title = 'Estoque'
admin.site.site_header = 'Sistema modelo de gestão de estoque'
admin.site.site_title = 'Sistema modelo de gestão de estoque'
