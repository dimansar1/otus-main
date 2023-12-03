from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class VideoForm(FlaskForm):
    name = StringField(
        label="Название видео",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    link = StringField(
        label="Ссылка на YouTube",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
