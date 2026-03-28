import os
from pathlib import Path

# BASE_DIR pointe vers le dossier racine (là où il y a manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Garde ta clé secrète actuelle
SECRET_KEY = 'django-insecure-2cjbui07(-+3ef3_6i1ach6=rna5o5w*!g*o%=(@)qspbx1%1o'

# Sécurité : DEBUG est False sur Render, True sur ton PC
DEBUG = 'RENDER' not in os.environ

# Autorise ton URL Render pour que le lien fonctionne
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
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# MODIFICATION : On ajoute le dossier parent SANGILIYAN pour que Django trouve les fichiers
ROOT_URLCONF = 'SANGILIYAN.Sangiliyan_2.urls'
WSGI_APPLICATION = 'SANGILIYAN.Sangiliyan_2.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'