"""
Django settings for djanvue_crm_django project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# reading .env file
env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR/'djanvue_crm_django'/'.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('APP_SECRET_KEY')


# Stripe pub key
STRIPE_PUB_KEY = env('STRIPE_PUB_KEY',)
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_PRICE_ID_FREE_PLAN = env('STRIPE_PRICE_ID_FREE_PLAN')
STRIPE_PRICE_ID_SMALL_TEAM = env('STRIPE_PRICE_ID_SMALL_TEAM')
STRIPE_PRICE_ID_LARGE_TEAM = env('STRIPE_PRICE_ID_LARGE_TEAM')
STRIPE_WEBHOOK_KEY = env('STRIPE_WEBHOOK_KEY')

FRONTEND_WEBSITE_SUCCESS_URL = f"{env('BASE_URL_FRONTEND')}/{env('FRONTEND_WEBSITE_SUCCESS_PATH')}"
FRONTEND_WEBSITE_CANCEL_URL = f"{env('BASE_URL_FRONTEND')}/{env('FRONTEND_WEBSITE_CANCEL_PATH')}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

CORS_ALLOWED_ORIGINS = [
    env('CORS_ALLOWED_ORIGINS', default='http://localhost:8080')]

CSRF_TRUSTED_ORIGINS = [
    env('CSRF_TRUSTED_ORIGINS', default='http://localhost:8080')]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # to test whitenoise locally
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # customs:
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'lead.apps.LeadConfig',
    'team.apps.TeamConfig',
    'client.apps.ClientConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # to serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # custom
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djanvue_crm_django.urls'

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

WSGI_APPLICATION = 'djanvue_crm_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
        'ENGINE': env('BDD_ENGINE'),
        'NAME': env('BDD_NAME'),
        'USER': env('BDD_USER'),
        'PASSWORD': env('BDD_PASSWORD'),
        'HOST': env('BDD_HOST'),
        'PORT': env('BDD_PORT', default=''),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# collecte toutes les resources statiques qui seront collectées grace à la commande py manage.py collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
