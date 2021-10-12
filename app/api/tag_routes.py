from flask import Blueprint, jsonify
from app.models import Tag, db


tag_routes = Blueprint('tags', __name__)


@tag_routes.route('/')
def tags():
    tags = Tag.query.all()
    return {'tags': [tag.to_dict() for tag in tags]}

