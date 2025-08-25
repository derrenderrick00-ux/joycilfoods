from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'replace-me'
DEBUG = False

ALLOWED_HOSTS = ['joycifoods.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'menu',
    'cart',
    'accounts'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'joycil_project.urls'

TEMPLATES = [
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR / 'templates'],
        'APP_DIRS':True,
        'OPTIONS':{
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_items_count',
            ]       
        }
    }
]

WSGI_APPLICATION = 'joycil_project.wsgi.application'

DATABASES = {'default':{'ENGINE':'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3'}}

AUTH_PASSWORD_VALIDATORS=[]
LANGUAGE_CODE='en-us'
TIME_ZONE='Africa/Nairobi'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL='/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # where your dev static files live
STATIC_ROOT = BASE_DIR / "staticfiles"  
MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR/'media'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # prints emails in console
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'

