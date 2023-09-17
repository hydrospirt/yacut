from http import HTTPStatus
from urllib.parse import urljoin
from flask import jsonify, request

from yacut.models import URLMap
from yacut.utils import generate_url

from yacut import app, db


@app.route('/api/id/<int:id>/', methods=['GET'])
def get_short_url(id):
    BASE_URL = request.url
    url = URLMap.query.get(id)
    if url is None:
        pass
    return jsonify({'url': urljoin(BASE_URL, url.to_dict()['short'])}), HTTPStatus.OK
