import re
from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db
from yacut.constants import REGULAR_EXPRESSION
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.views import get_unique_short_id


@app.route('/api/id/<string:short_url>/', methods=['GET'])
def get_url(short_url):
    url = URLMap.query.filter_by(short=short_url).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    data = url.to_dict()
    return jsonify({'url': data['url']}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if ('custom_id' not in data or
            data['custom_id'] == '' or
            data['custom_id'] is None):
        data['custom_id'] = get_unique_short_id()
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        custom_id = data['custom_id']
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    if (re.match(REGULAR_EXPRESSION, data['custom_id']) is None or
            len(data['custom_id']) > 16):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED
