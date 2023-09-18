from flask import render_template, flash, redirect, url_for

from yacut import app, db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.utils import generate_url, is_already_in_database


def add_to_db(form, short):
    url = URLMap(
        original=form.original.data,
        short=short
    )
    db.session.add(url)
    db.session.commit()
    return flash(url_for('url_view', short=url.short, _external=True))


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLForm()
    short = form.short.data
    if form.validate_on_submit():
        if short is None:
            short = generate_url()
            flash('Ваша новая ссылка готова:')
            add_to_db(form, short)
        if len(short) > 16:
            flash('Указано недопустимое имя для короткой ссылки')
        if is_already_in_database(short):
            flash(f'Имя {short} уже занято!')
            short = generate_url()
            add_to_db(form, short)
        else:
            flash('Ваша новая ссылка готова:')
            add_to_db(form, short)
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=('GET',))
def url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404().original
    return redirect(url)