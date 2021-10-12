from .db import db


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredientPhoto = db.Column(db.String)
    # many to one user
    authorId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', back_populates='recipes')
    # one to many comments
    comments = db.relationship('Comment', back_populates='recipe',
                               cascade="all, delete")
    # one to many instructions
    instructions = db.relationship('Instruction', back_populates='recipe',
                               cascade="all, delete")
    # one to many ingredients
    ingredients = db.relationship('Ingredient', back_populates='recipe',
                               cascade="all, delete")
    # one to many tags
    tags = db.relationship('Tag', back_populates='recipe',
                           cascade="all, delete")
    # one to many likes
    likes = db.relationship('Like', back_populates='recipe', cascade="all, delete")

    #one to many videos/media
    medias = db.relationship('Media', back_populates='recipe', cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'authorId': self.authorId,
            "author": self.author.to_dict(),
            "instructions": [instruction.to_dict() for instruction in self.instructions],
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients],
            "comments": [comment.to_dict() for comment in self.comments],
            "tags": [tag.to_dict() for tag in self.tags],
            "likes": [like.to_dict() for like in self.likes],
            "medias": [media.to_dict() for media in self.medias]
        }
