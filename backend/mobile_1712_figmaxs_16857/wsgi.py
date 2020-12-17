"""
WSGI config for mobile_1712_figmaxs_16857 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobile_1712_figmaxs_16857.settings')

application = get_wsgi_application()
