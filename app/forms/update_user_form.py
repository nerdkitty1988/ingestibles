from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import ValidationError
from app.models import User


class UpdateUserForm(FlaskForm):
    username = StringField(
        'username')
    email = StringField('email')
    password = StringField('password')
    biography = TextAreaField('biography')
    profilePic = StringField('profilePic')
