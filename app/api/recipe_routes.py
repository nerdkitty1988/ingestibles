from flask import Blueprint, jsonify
from app.models import Recipe, db


recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('/')
def recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route('/<int:id>')
def single_recipe(id):
    recipe = Recipe.query.filter_by(id=id).first()
    return {'recipe': [recipe.to_dict()]}
