import os

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

SECRET_KEY ='5$6crm+lfbkjyc6473@h7=v#h5&%&o@jq3shic15qa-6uw*gd-'