#encoding=utf-8
# Django settings for virtrael project.
import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG =True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'), --> ¡¡¡No omitir la , del final!!!
)

# Configuración del servidor de correo para envio de emails a los administradores
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vitadieta.info@gmail.com'
EMAIL_HOST_PASSWORD = '3w2UwNhp'
EMAIL_SUBJECT_PREFIX = '[Virtrael] '


MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'virtrael',    # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'hygea_admin',  
        'PASSWORD': 'hygea2011', 
        'HOST': 'localhost',
        'PORT': '', # Set to empty string for default.
        'OPTIONS': {
             "init_command": "SET foreign_key_checks = 0;",
        },
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ES'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = PROJECT_PATH + '/site_media/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/site_media/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/site_media/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "site_media/static/"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x#=auw=%k3&&62&@-$o^k^x&$x0-h1q@ni8cs#btsk_4#=3&_v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.app_directories.load_template_source'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    # Autenticacion externa (google)
    # 'social.apps.django_app.context_processors.backends',
    # 'social.apps.django_app.context_processors.login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django-crossdomainxhr-middleware.XsSharing',
)

ROOT_URLCONF = 'virtrael.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'virtrael.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + '/templates/'
)

JSTEMPLATE_DIRS = (
    # Templates handlebars para jstemplate
    PROJECT_PATH + '/templates/jstemplates/'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin', #administracion de django
    # 'django.contrib.admindocs',

    'bootstrap_admin', #look basado en bootstrap (www.getbootstrap.com) para la administracion de Django    
    'tastypie', #API de servicios WEB,
    'south',    #API para la gestión de la bd
    'virtrael_api' #Api RESTFUL para la base de datos virtrael
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
        'standard': {
            'format': '\n' + '[%(asctime)s] %(levelname)s [%(name)s/%(filename)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    
    'handlers': {
        # Handlers for production version
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'production_file': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': PROJECT_PATH + '/../log/virtrael.log',
            'maxBytes': 1024*1024*5,    # 5 MB
            'backupCount': 7
        },
        
        # Handlers for debug version
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'debug_file': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': PROJECT_PATH + '/../log/virtrael_debug.log',
            'maxBytes': 1024*1024*5,   # 5 MB
            'backupCount': 7
        },
        
        # Null handler
        'null': {
            'class': 'django.utils.log.NullHandler'
        }
    },
    
    'loggers': {
        'django.request': {
            'level': 'ERROR',
            'handlers': ['mail_admins', 'production_file', 'console', 'debug_file'],
            'propagate': True
        },
        'django': {
            'handlers': ['null', ]
        },
        'py.warnings': {
            'handlers': ['null', ]
        },
        'virtrael': {
            'level': 'DEBUG',
            'handlers': ['console', 'production_file', 'debug_file']
        }
    }
}


