"""
cpd_manager Project settings.
"""
from pathlib import Path

# Hosting settings.
SECRET_KEY = 'django-insecure-epk#6egroal=dunyzws%8^)9938!b6-klaz*8j6sg87yu-jh)m'
DEBUG = True
ALLOWED_HOSTS = []

# Application settings.
BASE_DIR = Path(__file__).resolve().parent.parent
INSTALLED_APPS = [
    "records",
    "users",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'cpd_manager.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'cpd_manager.wsgi.application'

# Database configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings.
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Africa/Johannesburg"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images).
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static/",
]

# Default primary key field type.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media file (pdf) configuration.
MEDIA_ROOT = BASE_DIR / "certifications"
MEDIA_URL = "/user_certificate/"

# User access variables.
LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = LOGIN_URL
