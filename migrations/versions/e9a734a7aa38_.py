"""empty message

Revision ID: e9a734a7aa38
Revises: a8e7c9a93644
Create Date: 2019-05-17 13:33:49.582773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9a734a7aa38'
down_revision = 'a8e7c9a93644'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'distcenter', ['public_id'])
    op.create_table('association',
    sa.Column('left_id', sa.String(length=100), nullable=True),
    sa.Column('right_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['left_id'], ['useradmin.public_id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['distcenter.public_id'], )
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'distcenter', type_='unique')
    op.drop_table('association')
    # ### end Alembic commands ###
