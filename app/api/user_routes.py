from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.forms.update_user_form import UpdateUserForm
from app.models import User, db
from app.api.auth_routes import validation_errors_to_error_messages
# setup AWS
from app.s3_helpers import (
    upload_file_to_s3, allowed_file, get_unique_filename)

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


@user_routes.route('/<int:id>', methods=["POST"])
@login_required
def updateUser(id):
    form = UpdateUserForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print('request.files!!!!', request.files)
    if form.validate_on_submit():
        user = User.query.get(id)

        user.username = form.data['username']
        user.email = form.data['email']
        user.biography = form.data['biography']
        # image/file to replace the original profile photo
        if 'profilePic' in request.files.keys():
            profilePic = request.files["profilePic"]

            if not allowed_file(profilePic.filename):
                return {"errors": ["profilePic file type not permitted"]}, 400

            profilePic.filename = get_unique_filename(
                profilePic.filename)

            upload_profilePic = upload_file_to_s3(profilePic)

            if "url" not in upload_profilePic:
                # if the dictionary doesn't have a url key
                # it means that there was an error when we tried to upload
                # so we send back that error message
                return {'errors': [upload_profilePic['errors']]}, 400

            profilePic_url = upload_profilePic["url"]
            user.profilePic = profilePic_url
        else:
            user.profilePic = user.profilePic

        if form.data['password']:
            user.password = form.data['password']

        db.session.commit()

        return user.to_dict()

    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@user_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def deleteUser(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user.to_dict()
