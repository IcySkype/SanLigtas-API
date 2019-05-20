"""empty message

Revision ID: df5a9d5ff9bd
Revises: 1cc0499d6711
Create Date: 2019-05-18 02:52:41.042076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df5a9d5ff9bd'
down_revision = '1cc0499d6711'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('distcenter', sa.Column('latitude', sa.FLOAT(), nullable=False))
    op.add_column('distcenter', sa.Column('longitude', sa.FLOAT(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('distcenter', 'longitude')
    op.drop_column('distcenter', 'latitude')
    # ### end Alembic commands ###
