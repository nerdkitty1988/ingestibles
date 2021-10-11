from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Recipe

create_recipe = Blueprint('create_recipe', __name__)


# post new recipes
@create_recipe.route('/', methods=['POST'])
@login_required
def createRecipe():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}

