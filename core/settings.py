import os
import re 
# from sw_utils.default_settings._installed_apps import *
from decouple import config
from django.utils.translation import gettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'corsheaders',
    'dal', 'dal_select2',
    'admin_auto_filters',
    'modeltranslation',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    # third-party
    "mptt",
    "tinymce",
    'ckeditor', 'ckeditor_uploader',
    'allauth','allauth.account','allauth.socialaccount', 'allauth.socialaccount.providers.google',
    'import_export',
    'rosetta',
    'colorfield',
    'adminsortable2',
    "rest_framework", 'rest_framework.authtoken', 'rest_framework_simplejwt',
    "rangefilter",
    'debug_toolbar',
    'nested_admin',
    # starway
    'sw_blog',
    'sw_cart',
    'sw_catalog',
    'sw_contact_form',
    'sw_content',
    'sw_currency',
    'sw_customer',
    'sw_global_config',
    'sw_imp_exp',
    'sw_liqpay',
    'sw_model_search',
    'sw_modelclone',
    'sw_novaposhta',
    'sw_order',
    'sw_solo',
    'sw_utils',
]
MIDDLEWARE = [
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'sw_utils.middleware.PutParsingMiddleware',
    'sw_utils.middleware.JSONParsingMiddleware',
    # 'sw_utils.middleware.DisableCSRF',
]
ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        # 'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sw_utils.context_processors.context',
                'sw_global_config.context_processors.context',
                # 'sw_cart.context_processors.context',
                # 'sw_catalog.context_processors.context',
            ],
            # 'loaders':[
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            #     # "admin_tools.template_loaders.Loader",
            # ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default':{
    #     'ENGINE':    'django.db.backends.postgresql_psycopg2',
    #     'NAME':      config('POSTGRES_DB_NAME'),
    #     'USER' :     config('POSTGRES_DB_USERNAME'),
    #     'PASSWORD' : config('POSTGRES_DB_PASSWORD'),
    #     'HOST' :     config('POSTGRES_DB_HOST') or '127.0.0.1',
    #     'PORT' :     config('POSTGRES_DB_PORT') or '5432',
    # },
}
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
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
LANGUAGES        = [
    ('uk', _('Українська')),
    ('en', _('Англійська')),
    ('ru', _('Російська')),
]

LOCALE_PATHS     = [os.path.join(BASE_DIR, 'locale'),]
LANGUAGE_CODE    = 'uk' # 'en-us'
TIME_ZONE        = 'UTC'
USE_I18N         = True
USE_L10N         = True
USE_TZ           = True
STATIC_URL       = '/static/'
SITE_ID          = 1
MEDIA_URL        = '/media/'
SECRET_KEY       = config('SECRET_KEY') 
DEBUG            = config('DEBUG', cast=bool) 
STATIC_ROOT      = os.path.join(BASE_DIR, "static_root")
MEDIA_ROOT       = os.path.join(BASE_DIR, "media")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]
ALLOWED_HOSTS    = ['*',]
INTERNAL_IPS     = ['127.0.0.1',]
DATE_FORMAT      = "d-m-Y H:M"
CKEDITOR_UPLOAD_PATH = ''
CORS_ORIGIN_ALLOW_ALL = True 
MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE
ROSETTA_MESSAGES_PER_PAGE = 100
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
AZURE_CLIENT_SECRET = "fa4b9549dca24df88eeb6c58ada57bed"

# mail
IGNORABLE_404_URLS = [
    re.compile(r'\.(php|cgi)$'),
    re.compile(r'^/phpmyadmin/'),
]
# EMAIL_BACKEND          = 'sw_global_config.backends.ConfiguredEmailBackend'
EMAIL_BACKEND          = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS          = True
EMAIL_USE_SSL          = False
EMAIL_PORT             = 587
EMAIL_HOST             = config('EMAIL_HOST')
EMAIL_HOST_USER        = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD    = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL     = EMAIL_HOST_USER
SERVER_EMAIL           = 'dev@starwayua.com'
ADMINS                 = [
    ('jurgeon018', 'jurgeon018@gmail.com'),
    ('DEV', 'dev@starwayua.com'),
]
MANAGERS = ADMINS 

# starway
LIQPAY_PUBLIC_KEY = "s"
LIQPAY_PRIVATE_KEY = "s"
LIQPAY_SANDBOX_PUBLIC_KEY = "s"
LIQPAY_SANDBOX_PRIVATE_KEY = "s"
LIQPAY_SANDBOX_MODE = 1

SITEMAP_PATHS = {
}
LOGIN_REDIRECT_URL    =  'profile'
LOGOUT_REDIRECT_URL   =  'index'
REGISTER_REDIRECT_URL =  'profile'




# tinymce
TINYMCE_DEFAULT_CONFIG = {
  'height': 360,
  # 'width': 920,
  'width': 'auto',
  # 'cleanup_on_startup': True,
  'cleanup_on_startup': False,
  'custom_undo_redo_levels': 20,
  'selector': 'textarea',
  'theme': 'modern',
  'plugins': '''
    textcolor save link image media preview codesample contextmenu
    table code lists fullscreen  insertdatetime  nonbreaking
    contextmenu directionality searchreplace wordcount visualblocks
    visualchars code fullscreen autolink lists  charmap print  hr
    anchor pagebreak
    ''',
  'toolbar1': '''
    fullscreen preview bold italic underline | formatselect fontselect,
    fontsizeselect  | forecolor backcolor | alignleft alignright |
    aligncenter alignjustify | indent outdent | bullist numlist table |
    | link image media | codesample |
    ''',
  'toolbar2': '''
    visualblocks visualchars |
    charmap hr pagebreak nonbreaking anchor |  code |
    ''',
  'contextmenu': 'formats | link image',
  'menubar': True,
  'statusbar': True,
  'inline': False,

}










