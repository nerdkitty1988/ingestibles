from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import User


def ingredientPhotoEmpty(form, field):
    # Checking if ingredientPhoto exists
    ingredientPhoto = field.data
    if ingredientPhoto == 'undefined' or ingredientPhoto == 'null':
        raise ValidationError('Ingredient Photo is required.')


class createRecipeForm(FlaskForm):
    authorId = IntegerField(
        'authorId', validators=[DataRequired()])
    recipeTitle = StringField(
        'recipeTitle', validators=[DataRequired()])
    introduction = StringField('introduction', validators=[DataRequired()])
    ingredientPhoto = StringField('ingredientPhoto',
                                  validators=[DataRequired(), ingredientPhotoEmpty])
    # require at least first tag is input
    tag1 = StringField('tag1', validators=[DataRequired()])
    # require at least first ingredient is input
    ingredient1 = StringField('ingredient1', validators=[DataRequired()])
    # require at least first media is input
    media1 = StringField('media1', validators=[DataRequired()])
    # steps = StringField('steps', validators=[DataRequired()])
