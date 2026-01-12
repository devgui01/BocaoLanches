"""
ASGI config for bocao_lanches project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bocao_lanches.settings')

application = get_asgi_application()
