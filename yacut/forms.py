from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from yacut.constants import REGULAR_EXPRESSION
from yacut.models import URLmap


class URL_Form(FlaskForm):
    original_link = URLField(
        'Введите оригинальную ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128),
                    URL(message='Проверьте корректность введёной ссылки')]
    )
    custom_id = StringField(
        'Введите короткий идентификатор',
        validators=[Optional(),
                    Length(1, 16),
                    Regexp(REGULAR_EXPRESSION, message='Только буквы и цифры')]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if URLmap.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')
