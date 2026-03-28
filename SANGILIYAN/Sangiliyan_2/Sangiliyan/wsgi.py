import os
from django.core.wsgi import get_wsgi_application

# CORRECTION FINALE : On utilise le chemin complet DossierParent.DossierProjet.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SANGILIYAN.Sangiliyan_2.settings')

application = get_wsgi_application()