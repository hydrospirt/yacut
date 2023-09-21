from flask import Response, flash, redirect, render_template, url_for

from yacut import app, db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.utils import generate_url, is_already_in_database


def add_to_db(form: URLForm, short: str) -> Response:
    url = URLMap(
        original=form.original.data,
        short=short
    )
    db.session.add(url)
    db.session.commit()
    return flash(url_for('url_view', short=url.short, _external=True))


@app.route('/', methods=('GET', 'POST'))
def index_view() -> Response:
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.short.data
    if short is None:
        short = generate_url()
    if short and len(short) > 16:
        flash('Указано недопустимое имя для короткой ссылки')
        return render_template('index.html', form=form)
    if text := is_already_in_database(short):
        flash(f'Имя {text} уже занято!')
        return render_template('index.html', form=form)
    flash('Ваша новая ссылка готова:')
    add_to_db(form, short)
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=('GET',))
def url_view(short: str) -> Response:
    url = URLMap.query.filter_by(short=short).first_or_404().original
    return redirect(url)