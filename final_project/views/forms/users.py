from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    username = StringField(
        label="Username:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    email = StringField(
        label="Email:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    password = StringField(
        label="Password:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    password2 = StringField(
        label="Repeat password:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )