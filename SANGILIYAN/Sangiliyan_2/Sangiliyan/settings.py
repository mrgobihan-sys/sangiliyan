from pathlib import Path
import os

# BASE_DIR pointe vers le dossier racine (là où il y a manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2cjbui07(-+3ef3_6i1ach6=rna5o5w*!g*o%=(@)qspbx1%1o'

# Passe à False automatiquement quand on est sur Render
DEBUG = 'RENDER' not in os.environ

# On autorise ton lien Render et ton PC local
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', 'sangiliyan.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Pour gérer le CSS en ligne
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ATTENTION : Doit correspondre au nom de ton dossier contenant urls.py
ROOT_URLCONF = 'Sangiliyan_2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

# ATTENTION : Doit correspondre au nom de ton dossier contenant wsgi.py
WSGI_APPLICATION = 'Sangiliyan_2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuration des fichiers Statiques
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Optionnel : désactive le stockage compressé si tu as des erreurs de build
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'