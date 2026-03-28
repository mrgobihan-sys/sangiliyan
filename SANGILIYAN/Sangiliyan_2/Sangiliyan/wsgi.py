import os
from django.core.wsgi import get_wsgi_application

# CORRECTION : On ajoute le _2 pour correspondre au nom de ton dossier
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sangiliyan_2.settings')

application = get_wsgi_application()