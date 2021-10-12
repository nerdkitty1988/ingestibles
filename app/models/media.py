from .db import db


class Media(db.Model):
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True)

    #COMMENT THIS IN ONCE RECIPES IS CREATED
    recipeId = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='medias')
    mediaUrl = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'mediaUrl': self.mediaUrl,
            'recipeId': self.recipeId
        }
