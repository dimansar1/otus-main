from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class VideoForm(FlaskForm):
    name = StringField(
        label="Video name:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    link = StringField(
        label="Video link:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
