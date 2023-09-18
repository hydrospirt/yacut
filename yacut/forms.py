from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField, StringField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLForm(FlaskForm):
    # Extremely long URLs are usually a mistake.
    # URLs over 2,000 characters will not work in the most popular web browsers.
    # Don't use them if you intend your site to work for the majority of Internet users.
    original = URLField(
        'Введите оригинальную ссылку',
        name='original_link',
        validators=(
            DataRequired(message='Обязательное поле'),
            Length(1, 2048),
            URL(require_tld=False, message='URL-адрес содержит ошибки')
        ))
    short = StringField(
        'Введите короткую ссылку до 16 символов',
        name='short_link',
        validators=(
            Optional(),
            Regexp(regex='^[a-zA-Z0-9_]*$',
                   message='Используйте только большие или маленькие латинские буквы, ' +
                   'цифры в диапазоне от 0 до 9')
        )
    )
    submit = SubmitField('Создать')
