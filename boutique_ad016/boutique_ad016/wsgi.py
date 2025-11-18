"""
WSGI config for boutique_ad016 project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boutique_ad016.settings')  # Make sure this says boutique_ad016

application = get_wsgi_application()
