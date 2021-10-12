"""empty message

Revision ID: 26ead50599aa
Revises: 76d1446af0e0
Create Date: 2021-10-11 22:28:51.541340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26ead50599aa'
down_revision = '76d1446af0e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'ingredientPhoto')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('ingredientPhoto', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
