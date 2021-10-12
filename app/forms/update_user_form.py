from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


class UpdateUserForm(FlaskForm):
    username = StringField(
        'username', validators=[username_exists])
    email = StringField('email', validators=[user_exists])
    password = StringField('password')
    biography = TextAreaField('biography')
    profilePic = StringField('profilePic')
