from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired


class createCommentForm(FlaskForm):
  userId = IntegerField(
      'userId', validators=[DataRequired()])
  recipeId = IntegerField(
      'recipeId', validators=[DataRequired()])
  comment = TextAreaField('comment', validators=[DataRequired()])
  #time_created = DateField('time_created', validators=[DataRequired()])
