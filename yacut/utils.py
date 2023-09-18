import random
import string
import re

from yacut.models import URLMap


def generate_url():
    """Генерирует строку из случайных символов [a-z],[A-Z],[0-9]"""
    GEN_LENGHT = 6
    random_string = ''.join(random.choices(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits, k=GEN_LENGHT
    ))
    return random_string


def is_already_in_database(short):
    """Проверяет запись в БД на уникальность значения"""
    if URLMap.query.filter_by(short=short).first():
        return True
    return False


def is_regex_custom_id_link(short):
    pattern = re.compile('^[a-zA-Z0-9_]*$')
    if pattern.match(short) and 6 <= len(short) > 16:
        return True
    return False