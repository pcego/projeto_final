from django.conf.urls import url
from core.views import home, board


urlpatterns = [
    url(r'^$', home, name='url_core_home'),
    url(r'^board/$', board, name='url_core_board'),
]
