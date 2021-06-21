import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MYSQLDB = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'osvet',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}