from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import User


def ingredientPhotoEmpty(form, field):
    # Checking if ingredientPhoto exists
    ingredientPhoto = field.data
    if ingredientPhoto == 'undefined':
        raise ValidationError('Ingredient Photo is required.')


class createRecipeForm(FlaskForm):
    authorId = IntegerField(
        'authorId', validators=[DataRequired()])
    title = StringField(
        'title', validators=[DataRequired()])
    introduction = StringField('introduction', validators=[DataRequired()])
    ingredientPhoto = StringField('ingredientPhoto',
                                  validators=[DataRequired(), ingredientPhotoEmpty])
    # tags = StringField('tags', validators=[DataRequired()])
    # media = StringField('media', validators=[DataRequired()])
    # ingredients = StringField('ingredients', validators=[DataRequired()])
    # steps = StringField('steps', validators=[DataRequired()])
