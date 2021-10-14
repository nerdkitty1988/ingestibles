from flask import Blueprint, jsonify, session, request
from app.models import Recipe, User, Like, db, Tag, Ingredient, Instruction, Media
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms import createRecipeForm
from app.forms import editRecipeForm

# setup AWS
from app.s3_helpers import (
    upload_file_to_s3, allowed_file, get_unique_filename)


recipe_routes = Blueprint('recipes', __name__)


@recipe_routes.route('/')
def recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route('/recent')
def recent_recipes():
    recipes = Recipe.query.order_by(Recipe.id.desc()).limit(5)
    return {"recent": [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route('/previous')
def previous_recipes():
    recipes = Recipe.query.order_by(Recipe.id.desc())
    return {"previous": [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route('/<int:id>')
def single_recipe(id):
    recipe = Recipe.query.filter_by(id=id).first()
    return {'recipe': [recipe.to_dict()]}

#Fetch user's like recipes
@recipe_routes.route('/my_plate/<int:id>')
@login_required
def user_recipes(id):
    created_recipes = Recipe.query.join(User).filter(User.id == id).all()
    liked_recipes = Recipe.query.join(Like).filter(Like.userId == id).all()
    return {'created': [created_recipe.to_dict() for created_recipe in created_recipes], 'liked': [liked_recipe.to_dict() for liked_recipe in liked_recipes]}


#Fetch recipe by tagId
@recipe_routes.route('/<tag>')
def recipes_by_tag(tag):
    tagged_recipes = Recipe.query.join(Tag).filter(Tag.name == tag).all()
    return {'tagged': [tagged_recipe.to_dict() for tagged_recipe in tagged_recipes]}


#To edit recipe, Fetch recipe by recipeId
@recipe_routes.route('/edit/<int:id>')
@login_required
def recipe_by_id_to_edit(id):
    recipe = Recipe.query.get(id)
    return recipe.to_dict()


# create new recipe
@recipe_routes.route('', methods=['POST'])
@login_required
def create_recipe():
    formRecipe = createRecipeForm()
    formRecipe['csrf_token'].data = request.cookies['csrf_token']
    # form.data has wts form class state variable; request.form has input excluding files/images; request.files has files/images
    # print('!!!!!!!!', formRecipe.data)
    # print('!!!!!!!!request.form', request.form)
    # print('!!!!!!!!request.files', request.files)

    # validate title and instructions of steps are not empty, because number of steps are not certain, thus cannot use wts-form to validate them
    for (key, value) in request.form.items():
        if key[0:4] == 'step':
            # e.g. step1_
            stepNumForValidation = key[4:].split('_')[0]
            stepPrefix = 'step' + stepNumForValidation + '_'
            # exclude not exit, '', all spaces
            if(( stepPrefix+'title' not in request.form.keys()) or (stepPrefix+'direction' not in request.form.keys()) or (not request.form[stepPrefix+'title']) or (not request.form[stepPrefix+'direction']) or request.form[stepPrefix+'title'].isspace() or request.form[stepPrefix+'direction'].isspace()):
                return {"errors": [f"{stepPrefix}title and {stepPrefix}direction are both required. Otherwise please leave them both empty, to exclude this step."]}, 400

    if formRecipe.validate_on_submit():

        if "ingredientPhoto" not in request.files:
            return {"errors": ["ingredientPhoto required"]}, 400

        ingredientPhoto = request.files["ingredientPhoto"]

        if not allowed_file(ingredientPhoto.filename):
            return {"errors": ["ingredientPhoto file type not permitted"]}, 400

        ingredientPhoto.filename = get_unique_filename(ingredientPhoto.filename)

        upload_ingredientPhoto = upload_file_to_s3(ingredientPhoto)
        # print('upload_ingredientPhoto!!!', upload_ingredientPhoto)
        # print('ingredientPhoto.content_type!!!!', ingredientPhoto.content_type)

        if "url" not in upload_ingredientPhoto:
            # if the dictionary doesn't have a url key
            # it means that there was an error when we tried to upload
            # so we send back that error message
            return {'errors': [upload_ingredientPhoto['errors']]}, 400

        ingredientPhoto_url = upload_ingredientPhoto["url"]

        recipe = Recipe(
            authorId=formRecipe.data['authorId'],
            title=formRecipe.data['recipeTitle'],
            description=formRecipe.data['introduction'],
            ingredientPhoto=ingredientPhoto_url
        )
        db.session.add(recipe)
        db.session.commit()

        # save tags; request.form is dictionary
        for (key, value) in request.form.items():
            if key[0:3] == 'tag':
                db.session.add(Tag(name=value, recipeId=recipe.id))

        # save ingredients; request.form is dictionary
        for (key, value) in request.form.items():
            # print('!!', key, value)
            if key[0:10] == 'ingredient':
                db.session.add(Ingredient(info=value, recipeId=recipe.id))

        # save media; request.form does not have imgages/file, request.file has files/images, is dictionary
        for (key, value) in request.files.items():
            if key[0:5] == 'media':
                media = request.files[key]
                if not allowed_file(media.filename):
                    return {"errors": [f"{key} file type not permitted"]}, 400

                media.filename = get_unique_filename(media.filename)

                upload_media = upload_file_to_s3(media)

                if "url" not in upload_media:
                    # if the dictionary doesn't have a url key
                    # it means that there was an error when we tried to upload
                    # so we send back that error message
                    return {'errors': [upload_media['errors']]}, 400

                media_url = upload_media["url"]
                db.session.add(Media(mediaUrl=media_url, recipeId=recipe.id))

        # save steps; request.form does not have imgages/file, request.file has files/images, is dictionary
        # e.g. step1_title step1_direction step1_photo as keys

        # to order steps by stepNumber
        stepToVisit = []
        for (key, value) in request.form.items():
            if key[0:4] == 'step':
                stepNumForVisit = int(key[4:].split('_')[0])
                if stepNumForVisit not in stepToVisit:
                    stepToVisit.append(stepNumForVisit)
        stepToVisit.sort()

        # stepNumberVisited = []
        for stepN in stepToVisit:
            # for (key, value) in request.form.items():
            #     if key[0:4] == 'step':
            #         stepNumber = key[4]
            # e.g. step1_
            stepPrefix = 'step'+str(stepN) + '_'

            # if(stepNumber not in stepNumberVisited):
            if(stepPrefix+'photo' in request.files.keys()):
                stepPhoto = request.files[stepPrefix+'photo']
                if not allowed_file(stepPhoto.filename):
                    return {"errors": [f"{stepPrefix}photo file type not permitted"]}, 400
                stepPhoto.filename = get_unique_filename(stepPhoto.filename)
                upload_stepPhoto = upload_file_to_s3(stepPhoto)
                if "url" not in upload_stepPhoto:
                    # if the dictionary doesn't have a url key
                    # it means that there was an error when we tried to upload
                    # so we send back that error message
                    return {'errors': [upload_stepPhoto['errors']]}, 400

                stepPhoto_url = upload_stepPhoto["url"]
            else:
                stepPhoto_url = None

            db.session.add(Instruction(imageUrl=stepPhoto_url, stepTitle=request.form[stepPrefix+'title'], directions=request.form[stepPrefix+'direction'], recipeId=recipe.id))
            # stepNumberVisited.append(stepNumber)
        db.session.commit()
        return recipe.to_dict()

    return {'errors': validation_errors_to_error_messages(formRecipe.errors)}, 400


# edit recipe
@recipe_routes.route('/edit/<int:id>', methods=['POST'])
@login_required
def edit_recipe(id):
    # query database to get book to edit
    # id comes from route
    recipe = Recipe.query.get(id)


    # if userId is not current logged-in user, no authorization
    if not recipe or recipe.authorId != current_user.to_dict()['id'] :
        return {'errors': ['No authorization.']}, 401

    formRecipe = editRecipeForm()
    formRecipe['csrf_token'].data = request.cookies['csrf_token']

    # form.data has wts form class state variable; request.form has input excluding files/images; request.files has files/images
    # print('!!!!!!!!formRecipe.data', formRecipe.data)
    # print('!!!!!!!!request.form', request.form)
    # print('!!!!!!!!request.files', request.files)

    # validate title and instructions of steps are not empty, because number of steps are not certain, thus cannot use wts-form to validate them

    for (key, value) in request.form.items():
        if key[0:4] == 'step':
            # e.g. step1_ ( step10_, key[0:7] )
            stepNumForValidation = key[4:].split('_')[0]
            stepPrefix = 'step' + stepNumForValidation +'_'
            # exclude not exit, '', all spaces
            if((stepPrefix+'title' not in request.form.keys()) or
                    (stepPrefix+'direction' not in request.form.keys()) or
                    (not request.form[stepPrefix+'title']) or
                    (not request.form[stepPrefix+'direction']) or
                    (request.form[stepPrefix+'title'].isspace()) or
                    (request.form[stepPrefix+'direction'].isspace())
                    ):
                # print('!!!!!eroor', key, value, stepPrefix +
                #       'title', request.form.keys(), stepPrefix +
                #       'title' not in request.form.keys())
                return {"errors": [f"{stepPrefix}title and {stepPrefix}direction are both required. Otherwise please leave them both empty, to exclude this step."]}, 400

    if formRecipe.validate_on_submit():
        # if ingredientPhoto is a file, not a string(an url), save to AWS and get its url in following if statement
        if not isinstance(formRecipe.data["ingredientPhoto"], str):
            # if "ingredientPhoto" not in request.files:
            # return {"errors": ["ingredientPhoto required"]}, 400

            ingredientPhoto = request.files["ingredientPhoto"]

            if not allowed_file(ingredientPhoto.filename):
                return {"errors": ["ingredientPhoto file type not permitted"]}, 400

            ingredientPhoto.filename = get_unique_filename(ingredientPhoto.filename)

            upload_ingredientPhoto = upload_file_to_s3(ingredientPhoto)
            # print('upload_ingredientPhoto!!!', upload_ingredientPhoto)
            # print('ingredientPhoto.content_type!!!!', ingredientPhoto.content_type)

            if "url" not in upload_ingredientPhoto:
                # if the dictionary doesn't have a url key
                # it means that there was an error when we tried to upload
                # so we send back that error message
                return {'errors': [upload_ingredientPhoto['errors']]}, 400

            ingredientPhoto_url = upload_ingredientPhoto["url"]
        else:
            ingredientPhoto_url = formRecipe.data["ingredientPhoto"]

        # edit recipe
        recipe.title = formRecipe.data['recipeTitle']
        recipe.description = formRecipe.data['introduction']
        recipe.ingredientPhoto = ingredientPhoto_url


        db.session.add(recipe)
        db.session.commit()


        # delete all its associated tags and save new tags; request.form is dictionary
        for tag in recipe.tags:
            db.session.delete(tag)

        for (key, value) in request.form.items():
            if key[0:3] == 'tag':
                db.session.add(Tag(name=value, recipeId=recipe.id))

        # delete all its associated ingredients and save new ingredients; request.form is dictionary
        for ingredient in recipe.ingredients:
            db.session.delete(ingredient)

        for (key, value) in request.form.items():
            if key[0:10] == 'ingredient' and key[10:15] != 'Photo':
                db.session.add(Ingredient(info=value, recipeId=recipe.id))

        # delete old media, and then save media; request.form has image url as string; request.file has files/images, is dictionary
        for media in recipe.medias:
            db.session.delete(media)
        for (key, value) in request.form.items():
            if key[0:5] == 'media':
                db.session.add(Media(mediaUrl=value, recipeId=recipe.id))

        for (key, value) in request.files.items():
            if key[0:5] == 'media':
                media = request.files[key]
                if not allowed_file(media.filename):
                    return {"errors": [f"{key} file type not permitted"]}, 400

                media.filename = get_unique_filename(media.filename)

                upload_media = upload_file_to_s3(media)

                if "url" not in upload_media:
                    # if the dictionary doesn't have a url key
                    # it means that there was an error when we tried to upload
                    # so we send back that error message
                    return {'errors': [upload_media['errors']]}, 400

                media_url = upload_media["url"]
                db.session.add(Media(mediaUrl=media_url, recipeId=recipe.id))

        # save steps; request.form does not have imgages/file, request.file has files/images, is dictionary
        # e.g. step1_title step1_direction step1_photo as keys
        for instruction in recipe.instructions:
            db.session.delete(instruction)

        # to order steps by stepNumber
        stepToVisit = []
        for (key, value) in request.form.items():
            if key[0:4] == 'step':
                stepNumForVisit = int(key[4:].split('_')[0])
                if stepNumForVisit not in stepToVisit:
                    stepToVisit.append(stepNumForVisit)
        stepToVisit.sort()


        for stepN in stepToVisit:
            # e.g. step1_
            stepPrefix = 'step'+str(stepN) + '_'
            if(stepPrefix+'photo' in request.files.keys()):
                stepPhoto = request.files[stepPrefix+'photo']
                if not allowed_file(stepPhoto.filename):
                    return {"errors": [f"{stepPrefix}photo file type not permitted"]}, 400
                stepPhoto.filename = get_unique_filename(stepPhoto.filename)
                upload_stepPhoto = upload_file_to_s3(stepPhoto)
                if "url" not in upload_stepPhoto:
                    # if the dictionary doesn't have a url key
                    # it means that there was an error when we tried to upload
                    # so we send back that error message
                    return {'errors': [upload_stepPhoto['errors']]}, 400

                stepPhoto_url = upload_stepPhoto["url"]
            elif(stepPrefix+'photo' in request.form.keys()):
                stepPhoto_url = request.form[stepPrefix+'photo']
            else:
                stepPhoto_url = None

            db.session.add(Instruction(imageUrl=stepPhoto_url, stepTitle=request.form[stepPrefix+'title'], directions=request.form[stepPrefix+'direction'], recipeId=recipe.id))



        db.session.commit()
        return recipe.to_dict()

    return {'errors': validation_errors_to_error_messages(formRecipe.errors)}, 400

# To delete recipe
@recipe_routes.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    if recipe.authorId != current_user.to_dict()['id'] or not recipe:
        return {'errors': ['No authorization.']}, 401

    db.session.delete(recipe)
    db.session.commit()
    return {'message': ['Delete Successfully']}
