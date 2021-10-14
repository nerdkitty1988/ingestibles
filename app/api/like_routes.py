from flask import Blueprint, jsonify, session, request
from app.models import Recipe, User, Like, db, Tag, Ingredient, Instruction, Media
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages


like_routes = Blueprint('likes', __name__)


@like_routes.route('/<int:id>', methods=['POST'])
@login_required
def post_like(id):
    recipe = Recipe.query.get(id)
    existingLikes = recipe.likes
    likes = Like.query.join(Recipe).filter(Recipe.id == id).all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}
