import os
import sys

# redirect stdout
sys.stdout = sys.stderr

os.environ['DJANGO_SETTINGS_MODULE'] = 'preprint.settings'

sys.path.append('/home/nick/biopreprints/preprint')
sys.path.append('/home/nick/biopreprints')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

