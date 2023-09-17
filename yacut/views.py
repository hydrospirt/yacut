import random
import string

from flask import render_template, flash

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


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short = form.short.data
        if short is None:
            short = generate_url()
        if URLMap.query.filter_by(short=short).first():
            flash('Такой адрес занят, для вас был сгенерирован другой адрес')
            short = generate_url()
        url = URLMap(
            original=form.original.data,
            short=short
        )
        db.session.add(url)
        db.session.commit()
    return render_template('index.html', form=form)