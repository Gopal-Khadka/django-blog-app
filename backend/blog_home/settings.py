"""
Django settings for blog_home project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os, logging
from pathlib import Path
from dotenv import load_dotenv
from filebrowser.sites import site

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "44ebca61af08a6763399c71acbb84ccb25233357cc4afa46c427c4e381eff78d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
X_FRAME_OPTIONS = "SAMEORIGIN"  # for django-grappelli to insert images in iframes
LOGIN_URL = "/login/"
# Application definition

INSTALLED_APPS = [
    "filebrowser",
    "django.contrib.admin",
    "grappelli",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "rest_framework",
    "rest_framework.authtoken",
    "tinymce",
    "easy_thumbnails",
    "algoliasearch_django",
    # "crispy_forms",
    # "crispy_bootstrap5",
    "corsheaders",
    # -------------------
    # my apps
    "blogs",
    "api",
    "forum",
    "stories",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "blog_home.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.static",
            ],
        },
    },
]

WSGI_APPLICATION = "blog_home.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"  # for production to serve static files

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# DJANGO ALL AUTH SETTINGS
AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "optional"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SOCIALACCOUNT_LOGIN_ON_GET = (
    True  # turns off all intermediate login prompts when signing up
)
if DEBUG:
    SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = [
        "http://localhost:8000/accounts/google/login/callback/flowName=GeneralOAuthFlow",
        "http://127.0.0.1:8000/accounts/google/login/callback/flowName=GeneralOAuthFlow",
    ]


# ALL AUTH GOOGLE CONFIGS
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "key": "",
        },
        "SCOPE": [
            # access profile info and email info from google
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}


# DJANGO LOGGING SETTINGS: https://docs.djangoproject.com/en/5.1/topics/logging/#id6

# Define the log directory
LOG_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "detailed": {
            "format": "{levelname} {asctime} {module} {message} {process:d} {thread:d} ",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "django_debug.log"),
            "formatter": "detailed",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "django_error.log"),
            "formatter": "verbose",
        },
        "debug_info_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "debug_info.log"),
            "formatter": "detailed",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "myapp": {
            "handlers": ["file", "debug_info_file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}


# MEDIA SETTINGS
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# TINYMCE SETTINGS
# TINYMCE_JS_URL = os.path.join(STATIC_URL, "js/tinymce/tinymce.min.js")
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": "320px",
    "width": "960px",
    "skin": "tinymce-5-dark",  # Set the UI skin
    "content_css": "tinymce-5-dark",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "en",  # To force a specific language instead of the Django current language.
}
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True  #
# TINYMCE_FILEBROWSER = True


# FILEBROWSER SETTINGS
site.directory = ""
site.storage.location = MEDIA_ROOT


# EASY THUMBNAIL SETTINGS

THUMBNAIL_DEBUG = True
THUMBNAIL_ALIASES = {
    "": {
        "avatar": {"size": (50, 50), "crop": True},
        "small": {"size": (100, 100), "crop": True},
        "medium": {"size": (300, 300), "crop": True},
        "large": {"size": (600, 600), "crop": True},
    },
}

THUMBNAIL_PROCESSORS = [
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "easy_thumbnails.processors.scale_and_crop",
    "easy_thumbnails.processors.filters",
]

THUMBNAIL_DEFAULT_OPTIONS = {
    "quality": 85,
    "format": "WEBP",
}


# Crispy Forms Settings
# CRISPY_ALLOWED_TEMPLATE_PACKS = ("bootstrap5", "bootstrap4", "bootstrap3")
# CRISPY_TEMPLATE_PACK = "bootstrap5"


# ALGOLIA SETTINGS
ALGOLIA = {
    "APPLICATION_ID": os.getenv("ALGOLIA_APPLICATION_ID"),
    "API_KEY": os.getenv("ALGOLIA_API_KEY"),
    "INDEX_PREFIX": "blogs",
}


# DJANG0-CORS-HEADERS
CORS_ALLOWED_ORIGINS = []
if DEBUG:
    CORS_ALLOWED_ORIGINS += [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]
# CORS_URLS_REGEX = r"^/api/.*$"
# CORS_ALLOW_ALL_ORIGINS = True
