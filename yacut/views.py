import random
import string

from flask import render_template, flash, redirect, url_for

from yacut import app, db
from yacut.forms import URLForm
from yacut.models import URLMap


def generate_url():
    gen_lenght = random.randrange(start=1,
                                  stop=16,
                                  step=1)
    random_string = ''.join(random.choices(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits, k=gen_lenght
    ))
    return random_string


def add_to_db(form, short):
    url = URLMap(
        original=form.original.data,
        short=short
    )
    db.session.add(url)
    db.session.commit()
    return flash(url_for('url_view', short=url.short, _external=True))


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    short = form.short.data
    if form.validate_on_submit():
        if short is None:
            short = generate_url()
            flash('Ваша новая ссылка готова:')
            add_to_db(form, short)
        if URLMap.query.filter_by(short=short).first():
            flash('Такой адрес занят, для вас был сгенерирован другой адрес:')
            short = generate_url()
            add_to_db(form, short)
        else:
            url = URLMap(
                original=form.original.data,
                short=short
            )
            db.session.add(url)
            db.session.commit()
            flash('Ваша новая ссылка готова:')
            add_to_db(form, short)
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404().original
    return redirect(url)