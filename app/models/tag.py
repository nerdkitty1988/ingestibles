from .db import db


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    # many to one recipe
    recipeId = db.Column(db.Integer, db.ForeignKey('recipes.id'),
                         nullable=False)
    recipe = db.relationship('Recipe', back_populates='tags')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'recipeId': self.recipeId,
        }
