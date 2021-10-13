from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.forms.update_user_form import UpdateUserForm
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>', methods=["GET", "PATCH"])
@login_required
def user(id, *updatedUser):
    user = User.query.get(id)
    if request.method == "PATCH":
            for k, v in updatedUser:
                user[k] = v
            return ({
                "id":user.id,
                "username":user.username,
                "email":user.email,
                "biography":user.biography,
                "profilePic":user.profilePic,
                "time_created":user.time_created
            })
    return user.to_dict()
