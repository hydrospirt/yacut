import random

from yacut.models import URLMap
from yacut.settings import GEN_LENGHT, GEN_SYMBOLS, MAXLEN_CUSTOM_ID, PATTERN


def generate_url() -> str:
    """Генерирует строку из шести случайных символов [a-z],[A-Z],[0-9]"""
    return ''.join(random.choices(GEN_SYMBOLS, k=GEN_LENGHT))


def is_already_in_database(short: str) -> str:
    """Проверяет запись в БД на уникальность значения"""
    if obj := URLMap.query.filter_by(short=short).first():
        return obj.short


def is_regex_custom_id_link(short: str) -> bool:
    """ Проверяет на соотвествие паттерну:
        - большие латинские буквы;
        - маленькие латинские буквы;
        - цифры в диапазоне от 0 до 9;
        - Не больше 16 символов;
    """
    return PATTERN.match(short) and len(short) > MAXLEN_CUSTOM_ID
