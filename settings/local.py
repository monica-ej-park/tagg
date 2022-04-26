from .base import *




DEBUG = True


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '172.30.1.13'
]


SESSION_COOKIE_DOMAIN=None

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1',
)

CSRF_TRUSTED_ORIGINS = [
    '.amazonaws.com',
    'localhost',
    '127.0.0.1',
    '172.30.1.13',
    ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'NAME': BASE_DIR / 'db.sqlite3',
    }
}


