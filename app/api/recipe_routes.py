from flask import Blueprint, jsonify
from app.models import Recipe, Tag, db


recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('/')
def recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route(f"/{Tag.name}")
def tag_recipes(name):
    tagged_recipes = Recipe.query.join(Tag).filter(Tag.name == name).all()
    print(tagged_recipes)
    return {'tagged': [tagged_recipe.to_dict() for tagged_recipe in tagged_recipes]}
