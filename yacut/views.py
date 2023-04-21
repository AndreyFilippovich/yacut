import random
import string

from flask import redirect, render_template

from yacut import app, db
from yacut.forms import URL_Form
from yacut.models import URLMap

LETTERS_COUNT = 6


def get_unique_short_id():
    letters_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_digits, LETTERS_COUNT))
    while URLMap.query.filter_by(short=rand_string).first():
        rand_string = ''.join(random.sample(letters_digits, LETTERS_COUNT))
    return rand_string


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_Form()
    if not form.validate_on_submit():
        return render_template('main.html', form=form)
    short_url = get_unique_short_id() 
    url = URLMap(
        original=form.original_link.data,
        short=short_url,
    )
    db.session.add(url)
    db.session.commit()
    context = {'form': form, 'short_url': short_url}
    return render_template('main.html', **context)


@app.route('/<string:short_url>')
def redirect_view(short_url):
    url = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(url.original)
