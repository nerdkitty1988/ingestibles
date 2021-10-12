from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from app.models import User


class newRecipeForm(FlaskForm):
    authorId = IntegerField(
        'authorId', validators=[DataRequired()])
    title = StringField(
        'title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    ingredientPhoto = StringField('ingredientPhoto',
                                  validators=[DataRequired()])
