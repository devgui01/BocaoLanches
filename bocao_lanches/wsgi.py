"""
WSGI config for bocao_lanches project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bocao_lanches.settings')

application = get_wsgi_application()
