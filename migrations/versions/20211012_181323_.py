"""empty message

Revision ID: 042fbca8a21e
Revises: 75939f703cfe
Create Date: 2021-10-12 18:13:23.305035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042fbca8a21e'
down_revision = '75939f703cfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instructions', sa.Column('directions', sa.Text(), nullable=False))
    op.add_column('media', sa.Column('mediaUrl', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('media', 'mediaUrl')
    op.drop_column('instructions', 'directions')
    # ### end Alembic commands ###
