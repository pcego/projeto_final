"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# intercepta a aplicação wsgi do django
# servindo os arquivos staticos quando o debug for false
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

# envolvendo o get_wsgi_application
application = Cling(get_wsgi_application())
