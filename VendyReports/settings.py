"""
Django settings for VendyReports project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-some-secret-key-for-development' # Replace with a strong key for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Update ALLOWED_HOSTS like this:
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.157']

# OR allow everyone (Only do this for local testing, not production)
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reports', # <-- YOUR NEW APPLICATION
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

ROOT_URLCONF = 'VendyReports.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'VendyReports.wsgi.application'


# Database Configuration (CRITICAL FOR YOUR PROJECT)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'watervendy',               # <-- REPLACE with your DB Name
        'USER': 'watervendy_user',          # <-- REPLACE with your DB Username
        'PASSWORD': 'vendyP@$5',            # <-- REPLACE with your DB Password
        'HOST': '128.199.89.72',            # <-- REPLACE with your DB IP Address
        'PORT': '3306',                     # MySQL default port
        'OPTIONS': {
            # Important for existing databases:
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# Password validation
# ... (standard Django settings) ...

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'