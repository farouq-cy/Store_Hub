"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6y!svxc#ynh52$al4&y^ql$u0kyob#s08+033t%oj)7ufui8w)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'pages.apps.PagesConfig',
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
ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/static')
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    'copyright': "STOREHUB",
    'site_title': "STOREHUB",
    'site_header': "STOREHUB",
    'site_brand': "STOREHUB",
    'site_icon': 'images/logo.png',
    "site_logo": 'images/logo.png',
#التحكم في حجم الصوره
    "site_logo_classes": "img-circle",
    
    "welcome_sign": "Welcome to STOREHUB Admin Panel",  # رسالة الترحيب

    # إعدادات القائمة الجانبية
    "show_sidebar": True,  # إظهار القائمة الجانبية
    "navigation_expanded": True,  # توسيع القائمة الجانبية تلقائيًا

    # إعدادات الألوان
    "theme": "dark",  # يمكنك استخدام "light" أو "dark"

    # إعدادات الرسوم البيانية
    "charts": [
        {
            "title": "Sales Report",
            "type": "bar",  # نوع الرسم (bar, line, pie, etc.)
            "data": {
                "labels": ["January", "February", "March", "April", "May", "June", "July"],
                "datasets": [
                    {
                        "label": "Sales",
                        "backgroundColor": "#79aec8",
                        "data": [65, 59, 80, 81, 56, 55, 40],
                    }
                ],
            },
        },
    ],    
        "charts": [
    {
        "title": "Product Sales",
        "type": "bar",
        "data": {
            "labels": ["Product A", "Product B", "Product C"],
            "datasets": [
                {
                    "label": "Sales",
                    "backgroundColor": "#79aec8",
                    "data": [100, 200, 150],  # بيانات مأخوذة من موديلاتك
                }
            ],
        },
    },
        {
            "title": "User Activity",
            "type": "line",
            "data": {
                "labels": ["January", "February", "March", "April", "May", "June", "July"],
                "datasets": [
                    {
                        "label": "Active Users",
                        "backgroundColor": "rgba(60,141,188,0.9)",
                        "data": [28, 48, 40, 19, 86, 27, 90],
                    }
                ],
            },
        },
    ],

    # إعدادات أخرى
    "changeform_format": "horizontal_tabs",  # تنسيق صفحة التعديل
    "related_modal_active": True,  # فتح النماذج ذات الصلة في نافذة منبثقة
}    

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
     "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
}

#media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'