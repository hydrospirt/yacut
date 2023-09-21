import os

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(APP_PATH, 'html/')
STATIC_DIR = os.path.join(APP_PATH, 'html/static')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY',
                           default='Зачем тебе секретный ключ?')
    JSON_AS_ASCII = False
