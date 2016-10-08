"""
Django settings for singesavant_shop project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar.defaults import *  # NOQA
from .site_settings import *  # NOQA

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%dsit@#o%)$8h1)mc4oymus4s+v_o+lg93+hi$%p9@f*!^r(t^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
from oscar import get_core_apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paypal',

    'django.contrib.flatpages',

    'compressor',
    'widget_tweaks'
] + get_core_apps(['apps.order', 'apps.shipping', 'apps.checkout'])

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

]

ROOT_URLCONF = 'singesavant_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'singesavant_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}



# OSCAR (e-commerce) config
from django.utils.translation import ugettext_lazy as _
OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': _('PayPal'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
    }
]

OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_SHOP_NAME = 'Le Singe Savant'
OSCAR_SHOP_TAGLINE = 'Brasserie urbaine de Lille'

OSCAR_ALLOW_ANON_REVIEWS = False
OSCAR_FROM_EMAIL = 'contact@singe-savant.com'
OSCAR_DEFAULT_CURRENCY = 'EUR'

OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name')

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Brewed', 'Conditioned', 'Ready To Ship', 'Shipped', 'Cancelled',),
    'Brewed': ('Conditioned', 'Cancelled'),
    'Conditioned': ('Ready To Ship', 'Cancelled'),
    'Ready To Ship': ('Shipped', 'Cancelled'),
    'Shipped': (),
    'Cancelled': (),
}


# PAYPAL
PAYPAL_SANDBOX_MODE = DEBUG
PAYPAL_CALLBACK_HTTPS = not DEBUG
PAYPAL_API_VERSION = '119'

PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'EUR'
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True



# Email configuration
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
