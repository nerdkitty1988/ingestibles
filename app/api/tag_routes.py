from flask import Blueprint, jsonify
from app.models import Tag, db
from  sqlalchemy.sql.expression import func, select


tag_routes = Blueprint('tags', __name__)


@tag_routes.route('/')
def tags():
    tags = Tag.query.all()
    return {'tags': [tag.to_dict() for tag in tags]}

@tag_routes.route('/random')
def random_tags():
    tags = Tag.query.order_by(func.random()).limit(5)
    return {"random": [tag.to_dict() for tag in tags]}
