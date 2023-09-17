from flask import render_template, flash, redirect, url_for

from yacut import app, db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.utils import generate_url


def add_to_db(form, short):
    url = URLMap(
        original=form.original.data,
        short=short
    )
    db.session.add(url)
    db.session.commit()
    return flash(url_for('url_view', short=url.short, _external=True))


def is_already_in_database(short):
    if URLMap.query.filter_by(short=short).first():
        return True
    return False


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    short = form.short.data
    print(short)
    if form.validate_on_submit():
        if short is None:
            short = generate_url()
            flash('Ваша новая ссылка готова:')
            add_to_db(form, short)
        if is_already_in_database(short):
            flash('Такой адрес занят.')
            flash('Для вас был сгенерирован другой адрес:')
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