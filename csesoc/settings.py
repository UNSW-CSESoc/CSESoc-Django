# Django settings for csesoc project.

import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

import csesoc_settings

if csesoc_settings.USE_REAL_EMAILS:
   CSESOC_SUGGEST_LIST = 'csesoc.suggestions@cse.unsw.edu.au'
   ADMINS = (
       ('Sysadmin Head', 'csesoc.sysadmin.head@csesoc.unsw.edu.au'),
   )
else:
   CSESOC_SUGGEST_LIST = csesoc_settings.MY_LOCAL_EMAIL
   ADMINS = (
       ('Sysadmin Head', csesoc_settings.MY_LOCAL_EMAIL),
   )

MANAGERS = ADMINS

FILE_UPLOAD_PERMISSIONS = 0644

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_PATH, 'db.sqlite3')           # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Mail Settings
SMTP_HOST = 'smtp.unsw.edu.au'
SMTP_PORT = '25'
SEND_BROKEN_LINKS = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Sydney'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-AU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL where the django authentication login view is accessible
LOGIN_URL = "/site/accounts/login"

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '../public/system')
STATIC_ROOT = os.path.join(PROJECT_PATH, '../public/static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'system/'
STATIC_URL = 'static/'

SITE_JS_ROOT = 'C:/workspace/python/csesoc/public/static/'
SITE_JS_URL = 'site_js/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

#WYSIWYG_ROOT = os.path.join(PROJECT_PATH,"../public/static/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = csesoc_settings.SETTINGS_SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    # 'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request', # we need this to provide the request variable to each template
    'csesoc.context_processors.sponsors_list',
    'csesoc.context_processors.media_url',
    'csesoc.context_processors.static_url',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'csesoc.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
    os.path.join(PROJECT_PATH, 'templates/murder'),
    os.path.join(PROJECT_PATH, 'templates/game'),
    os.path.join(PROJECT_PATH, 'templates/suggestions'),
    os.path.join(PROJECT_PATH, 'templates/music'),
    os.path.join(PROJECT_PATH, 'templates/polls'),
)

#TINYMCE_JS_URL = SITE_JS_URL +'js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = SITE_JS_ROOT +'/js/tiny_mce/'
TINYMCE_JS_URL = "http://www.csesoc.unsw.edu.au/tinymce/tiny_mce.js"
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'theme': "advanced",
	'theme_advanced_toolbar_location' : "top",
	'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
	'theme_advanced_resizing' : 'true',
}

TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'csesoc.helpers',
    'csesoc.mainsite',    
    'csesoc.campleaders',
    'csesoc.campattendees',
    'csesoc.scheduler',
    'csesoc.sponsors',
    'csesoc.suggestions',
    'csesoc.murder',
    'csesoc.game',
    'csesoc.music',
    'csesoc.polls',
	'tinymce',
)

AUTHENTICATION_BACKENDS = (
    'csesoc.auth.backends.CSEBackend',
    #'django.contrib.auth.backends.ModelBackend',
)

# maxiumum number of StreamItems per paginated index page
STREAMITEMS_PER_PAGE = 5

