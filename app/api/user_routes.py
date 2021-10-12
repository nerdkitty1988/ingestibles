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
def user(id):
    form = UpdateUserForm()
    user = User.query.get(id)
    if request.method == "PATCH":
        if form.validate_on_submit():
            for k, v in form.data:
                user[k] = v
            return
    return user.to_dict()
