from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from app.models import User


class createRecipeForm(FlaskForm):
    authorId = IntegerField(
        'authorId', validators=[DataRequired()])
    title = StringField(
        'title', validators=[DataRequired()])
    introduction = StringField('introduction', validators=[DataRequired()])
    ingredientPhoto = StringField('ingredientPhoto',
                                  validators=[DataRequired()])
    tags = StringField('tags', validators=[DataRequired()])
    media = StringField('media', validators=[DataRequired()])
    ingredients = StringField('ingredients', validators=[DataRequired()])
    steps = StringField('steps', validators=[DataRequired()])
