"""
Django settings for todo project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

#ver minuto 27: https://www.youtube.com/watch?v=8l8xwvRO1_U&t=1920s ###

#para o output Everything up-to-date: https://pt.stackoverflow.com/questions/52651/git-n%C3%A3o-envia-commits-para-servidor-erro-everything-up-to-date


#msgTeste
#ksksks
#dfrfr
#ggggg
#kkkkkh
#https://stackoverflow.com/questions/21947406/git-push-heroku-master-says-everything-up-to-date-but-the-app-is-not-current


import os
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ktv-0k(og2h1eqna-u8yuo@*kvx@h3@-5@e4hf-1ic32zbo82f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://bity-chamados2.herokuapp.com/'] #https://chamadosapp.herokuapp.com/

# Application definition #app #app
#

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chamados_gerais',
    'about',
    'users',
    'crispy_forms',
    'accounts',
  
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

ROOT_URLCONF = 'todo.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'todo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# config da hora
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'Brazil/East' 

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Arquivos de media/upload
MEDIA_ROOT = os.path.join(BASE_DIR, 'midia') #caminho absoluto da url
MEDIA_URL = '/midia/' # Aqui basicamente gera um link para clicar e visualizar o anexo recebido/enviado!

#O comando abaixo serve para deixar o crispy_forms estilizado com bootstrap4
CRISPY_TEMPLATE_PACK = 'bootstrap4' #or bootstrap3
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
## frfrfr

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())
