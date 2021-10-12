from flask import Blueprint, jsonify, session, request
from app.models import Recipe, User, Like, db
from flask_login import login_required
from app.api.auth_routes import validation_errors_to_error_messages


recipe_routes = Blueprint('recipes', __name__)


@recipe_routes.route('/')
def recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route('/my_plate/<int:id>')
@login_required
def user_recipes(id):
    created_recipes = Recipe.query.join(User).filter(User.id == id).all()
    print(created_recipes)
    liked_recipes = Recipe.query.join(Like).filter(Like.userId == id).all()
    print(liked_recipes)
    return {'liked': [created_recipe.to_dict() for created_recipe in created_recipes], 'created': [liked_recipe.to_dict() for liked_recipe in liked_recipes]}


# create new recipe
@recipe_routes.route('/', methods=['POST'])
@login_required
def create_recipe():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}