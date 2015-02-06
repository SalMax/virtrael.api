import os
import sys

path = '/var/www/hygea.api'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'hygea.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
