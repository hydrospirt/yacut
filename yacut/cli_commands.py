import csv

import click

from yacut import app, db
from yacut.models import URLMap
from yacut.utils import generate_url


def load_to_database(row, counter):
    """Функция записи в базу данных, возвращает количество записанных обьектов"""
    url = URLMap(**row)
    db.session.add(url)
    db.session.commit()
    counter += 1
    return counter


@app.cli.command('load_links')
def load_links_command():
    """Функция загрузки ссылок в базу данных."""
    with open('links.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            if URLMap.query.filter_by(short=row['short']).first():
                row['short'] = generate_url()
                counter = load_to_database(row, counter)
            if not row['short']:
                row['short'] = generate_url()
                counter = load_to_database(row, counter)
            else:
                url = URLMap(**row)
                db.session.add(url)
                db.session.commit()
                counter = load_to_database(row, counter)
    click.echo(f'Загружено ссылок в базу данных: {counter}')
