"""empty message

Revision ID: 4e2ff13845ab
Revises: b67e37588d91
Create Date: 2019-04-15 15:12:46.928024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e2ff13845ab'
down_revision = 'b67e37588d91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['last_name'])
    op.create_unique_constraint(None, 'user', ['first_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###
