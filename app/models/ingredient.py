from .db import db


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)


    # COMMENT THIS IN ONCE RECIPES IS CREATED
    recipeId = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='ingredients')

    info = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'recipeId': self.recipeId,
            'info': self.info
        }
