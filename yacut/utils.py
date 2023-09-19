import random
import string
import re

from yacut.models import URLMap


def generate_url():
    """Генерирует строку из шести случайных символов [a-z],[A-Z],[0-9]"""
    GEN_LENGHT = 6
    random_string = ''.join(random.choices(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits, k=GEN_LENGHT
    ))
    return random_string


def is_already_in_database(short):
    """Проверяет запись в БД на уникальность значения"""
    if obj := URLMap.query.filter_by(short=short).first():
        return obj.short
    return False


def is_regex_custom_id_link(short):
    """ Проверяет на соотвествие паттерну:
        - большие латинские буквы;
        - маленькие латинские буквы;
        - цифры в диапазоне от 0 до 9;
        - Не больше 16 символов;
    """
    pattern = re.compile('[a-zA-Z0-9]*$')
    if pattern.match(short) and len(short) <= 16:
        return False
    return True
