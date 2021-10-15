from flask import Blueprint, jsonify, session, request
from app.models import Recipe, User, Like, db, Tag, Ingredient, Instruction, Media
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages


like_routes = Blueprint('likes', __name__)


@like_routes.route('/<int:id>', methods=['POST'])
@login_required
def post_like(id):
    likedbefore = Like.query.filter_by(
        recipeId=id, userId=int(current_user.to_dict()['id'])).first()

    if not likedbefore:
        like = Like(recipeId=id, userId=int(current_user.to_dict()['id']))
        db.session.add(like)
        db.session.commit()
        return {'like': 'like'}
    else:
        db.session.delete(likedbefore)
        db.session.commit()
        return {'unlike': 'unlike'}


@like_routes.route('/<int:id>')
@login_required
def get_like(id):
    likedbefore = Like.query.filter_by(
        recipeId=id, userId=int(current_user.to_dict()['id'])).first()

    if not likedbefore:
        return {'unlike': 'unlike'}
    else:
        return {'like': 'like'}
        
