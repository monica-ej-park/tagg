from .base import *


DEBUG = True

ALLOWED_HOSTS = [
    '.amazonaws.com',
    'localhost',
    '127.0.0.1',
    'samsungtablab.com',
    '.samsungtablab.com',
    ]

CSRF_COOKIE_DOMAIN = '.samsungtablab.com'
SESSION_COOKIE_DOMAIN = '.samsungtablab.com'

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8000',
    'http://127.0.0.1',
    'http://samsungtablab.com',
    'https://samsungtablab.com',
    'https://api.samsungtablab.com',
    'http://api.samsungtablab.com',
    'http://samsung-tablab-dataviz.s3-website.ap-northeast-2.amazonaws.com' # TODO 데이터시각화 데모용 url. 삭제 예정
)

CSRF_TRUSTED_ORIGINS = [
    'samsungtablab.com',
    '.samsungtablab.com',
    '.amazonaws.com',
    'localhost',
    '127.0.0.1',
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'samsungtablab',
        'USER': 'nolgong',
        'PASSWORD': 'noler1233',
        'HOST': 'samsungtablab.c9rmto62xi2l.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}

LOGIN_REDIRECT_URL = 'https://samsungtablab.com'
