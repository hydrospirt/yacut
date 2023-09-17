from http import HTTPStatus
from urllib.parse import urljoin

from flask import jsonify, request

from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import generate_url


@app.route('/api/id/<int:id>/', methods=['GET'])
def get_short_url(id):
    BASE_URL = request.url
    url = URLMap.query.get(id)
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': urljoin(BASE_URL, url.to_dict()['short'])}), HTTPStatus.OK
