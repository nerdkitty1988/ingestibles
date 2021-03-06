"""empty message

Revision ID: 76d1446af0e0
Revises: 3a8a6ae94e88
Create Date: 2021-10-11 19:57:09.048736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76d1446af0e0'
down_revision = '3a8a6ae94e88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('ingredientPhoto', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'ingredientPhoto')
    # ### end Alembic commands ###
