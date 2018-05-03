import os
import sys
from django.core.wsgi import get_wsgi_application
import django

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'Converte.settings'

sys.stdout = sys.stderr

DEBUG = True

application = get_wsgi_application()

django.setup()
