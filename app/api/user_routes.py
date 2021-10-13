from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.forms.update_user_form import UpdateUserForm
from app.models import User, db
from app.api.auth_routes import validation_errors_to_error_messages

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/<int:id>', methods=["PATCH"])
@login_required
def updateUser(id):
    form = UpdateUserForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User.query.get(id)

        user.username = form.data['username']
        user.email = form.data['email']
        user.biography = form.data['biography']
        user.profilePic = form.data['profilePic']
        if form.data['password']:
            user.password = form.data['password']

        db.session.commit()

        return user.to_dict()

    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400
