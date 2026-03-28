import os
from django.core.wsgi import get_wsgi_application

# On enlève le préfixe 'sangiliyan.' pour que Django cherche 
# directement le dossier 'Sangiliyan_2' à la racine.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sangiliyan_2.settings')

application = get_wsgi_application()