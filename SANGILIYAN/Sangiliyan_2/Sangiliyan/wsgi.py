import os
from django.core.wsgi import get_wsgi_application

# On utilise 'sangiliyan' en minuscules ici aussi
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sangiliyan.Sangiliyan_2.settings')

application = get_wsgi_application()