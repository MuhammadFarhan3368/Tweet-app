import sys
import os

try:
    from django.core.wsgi import get_wsgi_application
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tweet-app.settings")

    app = get_wsgi_application()

except Exception as e:
    print("ERROR:", str(e))  # This will show in Vercel logs
    raise
