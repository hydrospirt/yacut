from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Optional, Regexp


class URLForm(FlaskForm):
    original = URLField(
        'Введите оригинальную ссылку',
        name='original_link',
        validators=(
            DataRequired(message='Обязательное поле'),
            URL(require_tld=False, message='URL-адрес содержит ошибки')
        ))
    short = StringField(
        'Введите короткую ссылку до 16 символов',
        name='custom_id',
        validators=(
            Optional(),
            Regexp(regex='^[a-zA-Z0-9_]*$',
                   message='Используйте только большие или маленькие латинские буквы, ' +
                   'цифры в диапазоне от 0 до 9')
        )
    )
    submit = SubmitField('Создать')
