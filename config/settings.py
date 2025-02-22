import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ('django-insecure-gigff)=(os801e#h8z6(6q!_()-v1f9m5zsk7xohl&l1b#77^_')
DEBUG =True
ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'udemy.CustomUser'
INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'udemy',
    'rest_framework',
    'corsheaders',

]



DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'




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

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Bishkek'
USE_L10N = True
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join( STATIC_URL)
MEDIA_ROOT = os.path.join('media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('ky', 'Kyrgyz'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ru', 'ky')
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3080",
    "http://127.0.0.3000",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

STRIPE_PUBLIC_KEY = "pk_test_51QeLyaPrZtds7DEWNd5ARixTDn7JIgn4xShk8Jrlpr6zhfRm8nmv3JlstV2ONVKOBJhLfjKHIsYePHAKqk1eJq6S00xr3h06nH"
STRIPE_SECRET_KEY = "sk_test_51QeLyaPrZtds7DEWf4wnbDM6NmHdRojpqL8Eu67dgLfvHlFtb2YGEqoX0Ol7T4tqEr6wA0wy7V0aMnJDBbVMkvwl00yQ0ZsfpR"




CORS_ALLOW_ALL_ORIGINS = True
