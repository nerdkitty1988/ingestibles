from flask import Blueprint, jsonify
from app.models import Recipe, User, Like, db
from flask_login import login_required


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
