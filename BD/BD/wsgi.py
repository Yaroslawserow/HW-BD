"""
WSGI config for BD project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from app.Create_Tables import create_Tables
create_Tables()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BD.settings")

application = get_wsgi_application()
