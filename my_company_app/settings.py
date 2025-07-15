"""
Django settings for my_company_app project.
"""

from pathlib import Path
import os

# Base directory for the project.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)dje3h1z0tj_1l%mwcoi4b+%8izqw!he$%r=2%t#gn6u8bpc=h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    'common_app',
    'admin_app',
    'manager_app',
    'hr_app',
    'employee_app',
    'client_app',
    'django_extensions',
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

ROOT_URLCONF = 'my_company_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'common_app', 'templates'), # For common_app templates like base_dashboard.html, login.html, home.html
            os.path.join(BASE_DIR, 'admin_app', 'templates'),  # For admin_app templates
            os.path.join(BASE_DIR, 'manager_app', 'templates'),# <--- ADD THIS LINE FOR MANAGER APP
            os.path.join(BASE_DIR, 'hr_app', 'templates'),     # For HR app templates
            os.path.join(BASE_DIR, 'employee_app', 'templates'),# For Employee app templates
            os.path.join(BASE_DIR, 'client_app', 'templates'),
        ],
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'my_company_app.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev', # Project-level static assets
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'common_app.CustomUser'

# Media files (user uploads)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Custom Authentication & Session Settings ---

# URL to redirect to when login is required
LOGIN_URL = '/common/login/' # Use the URL path, not the URL name

# Session expires when browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Session cookie security (set to True in production with HTTPS)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False