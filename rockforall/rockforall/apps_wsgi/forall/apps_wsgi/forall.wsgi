import os, sys
sys.path.append('/home/forallwiki/apps_wsgi')
sys.path.append('/home/forallwiki/apps_wsgi/forall')
os.environ['PYTHON_EGG_CACHE'] = '/home/forallwiki/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'forall.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
