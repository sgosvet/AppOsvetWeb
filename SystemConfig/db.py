import os
import dj_database_url
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# MySQL
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

# HEROKU database configuration
HEROKU_DB = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}