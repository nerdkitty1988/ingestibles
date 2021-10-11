"""empty message

Revision ID: 0304c6b3682a
Revises: eeb66aba3dd5
Create Date: 2021-10-11 12:15:05.362141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0304c6b3682a'
down_revision = 'eeb66aba3dd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('mediaUrl', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('biography', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('profilePic', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profilePic')
    op.drop_column('users', 'biography')
    op.drop_table('media')
    op.drop_table('likes')
    # ### end Alembic commands ###
