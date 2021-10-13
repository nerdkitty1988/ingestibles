from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    username = form.data["username"]
    user = User.query.filter(User.email == email and User.username != username).first()
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
        'username')
    email = StringField('email')
    biography = TextAreaField('biography')
    profilePic = StringField('profilePic')
