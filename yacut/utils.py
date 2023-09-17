import random
import string


def generate_url():
    """Генерирует строку из случайных символов [a-z],[A-Z],[0-9]"""
    gen_lenght = random.randrange(start=1,
                                  stop=16,
                                  step=1)
    random_string = ''.join(random.choices(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits, k=gen_lenght
    ))
    return random_string
