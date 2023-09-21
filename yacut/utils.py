import random

from yacut.models import URLMap
from yacut.settings import GEN_LENGHT, GEN_SYMBOLS, MAXLEN_CUSTOM_ID, PATTERN


def generate_url():
    """Генерирует строку из шести случайных символов [a-z],[A-Z],[0-9]"""
    random_string = ''.join(
        random.choices(GEN_SYMBOLS, k=GEN_LENGHT))
    return random_string


def is_already_in_database(short):
    """Проверяет запись в БД на уникальность значения"""
    if obj := URLMap.query.filter_by(short=short).first():
        return obj.short


def is_regex_custom_id_link(short):
    """ Проверяет на соотвествие паттерну:
        - большие латинские буквы;
        - маленькие латинские буквы;
        - цифры в диапазоне от 0 до 9;
        - Не больше 16 символов;
    """
    return PATTERN.match(short) and len(short) >= MAXLEN_CUSTOM_ID
