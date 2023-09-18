from http import HTTPStatus
from urllib.parse import urljoin

from flask import jsonify, request

from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import generate_url, is_already_in_database, is_regex_custom_id_link


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url.to_dict()['original']}), HTTPStatus.OK


@app.route('/api/id/', methods=('POST',))
def create_short_url():
    BASE_URL = request.host_url
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!', HTTPStatus.BAD_REQUEST)
    if data.get('custom_id') and is_regex_custom_id_link(data.get('custom_id')):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', HTTPStatus.BAD_REQUEST)
    if data.get('custom_id') and is_already_in_database(data.get('custom_id')):
        raise InvalidAPIUsage(f'Имя "{data.get("custom_id")}" уже занято.', HTTPStatus.BAD_REQUEST)
    if not data.get('custom_id'):
        data['custom_id'] = generate_url()
        url = URLMap()
        url.from_dict(data)
        db.session.add(url)
        db.session.commit()
        return jsonify(
            {'url': url.to_dict()['original'],
             'short_link': urljoin(BASE_URL, url.to_dict()['short'])
             }), HTTPStatus.CREATED
    else:
        url = URLMap()
        url.from_dict(data)
        db.session.add(url)
        db.session.commit()
        return jsonify(
            {'url': url.to_dict()['original'],
             'short_link': urljoin(BASE_URL, url.to_dict()['short'])
             }), HTTPStatus.CREATED
