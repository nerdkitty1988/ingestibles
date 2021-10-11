from flask import Blueprint, jsonify
from app.models import Recipe, db


recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('/')
def recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}


