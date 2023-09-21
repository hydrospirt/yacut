import os
import re
import string

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(APP_PATH, 'html/')
STATIC_DIR = os.path.join(APP_PATH, 'html/static')
GEN_SYMBOLS = (string.ascii_uppercase +
               string.ascii_lowercase +
               string.digits)
GEN_LENGHT = 6
PATTERN = re.compile('[a-zA-Z0-9]*$')
MAXLEN_CUSTOM_ID = 16


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY',
                           default='QAZwsx123')
    JSON_AS_ASCII = False
