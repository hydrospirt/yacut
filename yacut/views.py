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

    if form.validate_on_submit():
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
def url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404().original
    return redirect(url)