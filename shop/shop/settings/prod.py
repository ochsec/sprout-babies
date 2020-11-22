import os
from .base import *
# from dotenv import load_dotenv

# load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('PROD_SECRET_KEY') 
SECRET_KEY = 'Gj%#4%TJAw3FNY&?!@9Uz4?`McU*<aGxNfjtvi*@vC`VuJ%!kD'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sprout-dev',
        'USER': 'doadmin',
        'PASSWORD': 'alt98m9u4wquaeyx',
        'HOST': 'db-postgresql-sfo2-98569-do-user-1287700-0.b.db.ondigitalocean.com',
        'PORT': 25060
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sproutbabies2@gmail.com'
EMAIL_HOST_PASSWORD = 'erEhG7b4QQ3j<H'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Braintree settings
BRAINTREE_MERCHANT_ID = 'vmb2qqxsjqzk2z84' # Merchant ID
BRAINTREE_PUBLIC_KEY = 'k44ztpp5sg5ygc2d' # Public key
BRAINTREE_PRIVATE_KEY = '903b70d305baa7a93b7ddd118fa630d7' # Private key

import braintree

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY,
)
