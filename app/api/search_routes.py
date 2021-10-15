from flask import Blueprint, jsonify
from app.models import Tag, Recipe, Ingredient


search_routes = Blueprint('search', __name__)


@search_routes.route('/<searchTerm>')
def searchResults(searchTerm):
    recipes_by_name = Recipe.query.filter(Recipe.title.ilike(f'%{searchTerm}%'))
    name_list = [recipe.to_dict() for recipe in recipes_by_name]
    recipes_by_tag = Recipe.query.join(Tag).filter(Tag.name.ilike(f'%{searchTerm}%'))
    tag_list = [recipe.to_dict() for recipe in recipes_by_tag]
    recipes_by_ingredient = Recipe.query.join(Ingredient).filter(Ingredient.info.ilike(f'%{searchTerm}%'))
    ingredient_list = [recipe.to_dict() for recipe in recipes_by_ingredient]
    return {
        'recipes': [*name_list, *tag_list, *ingredient_list]

    }
