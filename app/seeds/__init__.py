from flask.cli import AppGroup
from .users import seed_users, undo_users
from .comments import seed_comments, undo_comments
from .instructions import seed_instructions, undo_instructions
from .ingredients import seed_ingredients, undo_ingredients
from .recipes import seed_recipes, undo_recipes
from .tags import seed_tags, undo_tags
from .likes import seed_likes, undo_likes
from .media import seed_media, undo_media

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_recipes()
    seed_tags()
    seed_comments()
    seed_instructions()
    seed_ingredients()
    seed_likes()
    seed_media()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_recipes()
    undo_tags()
    undo_comments()
    undo_instructions()
    undo_ingredients()
    undo_likes()
    undo_media()
    # Add other undo functions here
