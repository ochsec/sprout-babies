import os
from .base import *
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DEV_SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Braintree settings
BRAINTREE_MERCHANT_ID = os.getenv('DEV_BRAINTREE_MERCHANT_ID') # Merchant ID
BRAINTREE_PUBLIC_KEY = os.getenv('DEV_BRAINTREE_PUBLIC_KEY') # Public key
BRAINTREE_PRIVATE_KEY = os.getenv('DEV_BRAINTREE_PRIVATE_KEY') # Private key

import braintree

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY,
)
