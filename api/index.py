from django.core.wsgi import get_wsgi_application
import sys
import os

# Setup environment
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

app = get_wsgi_application()
# This is the WSGI configuration for your Django project.