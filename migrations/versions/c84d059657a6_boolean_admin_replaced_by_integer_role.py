"""Boolean Admin replaced by Integer Role

Revision ID: c84d059657a6
Revises: e6b81f9793c7
Create Date: 2019-04-15 14:50:42.045219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c84d059657a6'
down_revision = 'e6b81f9793c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.Integer(), nullable=False))
    op.drop_column('user', 'admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('user', 'role')
    # ### end Alembic commands ###
