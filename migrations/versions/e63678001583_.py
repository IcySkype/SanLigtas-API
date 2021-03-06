"""empty message

Revision ID: e63678001583
Revises: 7abfd4a9666b
Create Date: 2019-08-08 00:56:40.841757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e63678001583'
down_revision = '7abfd4a9666b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('household',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(length=300), nullable=False),
    sa.Column('public_id', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('public_id')
    )
    op.drop_table('dependents')
    op.add_column('evacuees', sa.Column('is_house_leader', sa.Boolean(), nullable=True))
    op.add_column('evacuees', sa.Column('public_id', sa.String(length=300), nullable=False))
    op.drop_constraint('evacuees_home_id_key', 'evacuees', type_='unique')
    op.create_unique_constraint(None, 'evacuees', ['public_id'])
    op.create_foreign_key(None, 'evacuees', 'household', ['home_id'], ['public_id'])
    op.drop_column('evacuees', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('evacuees', sa.Column('address', sa.VARCHAR(length=300), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'evacuees', type_='foreignkey')
    op.drop_constraint(None, 'evacuees', type_='unique')
    op.create_unique_constraint('evacuees_home_id_key', 'evacuees', ['home_id'])
    op.drop_column('evacuees', 'public_id')
    op.drop_column('evacuees', 'is_house_leader')
    op.create_table('dependents',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('dependents_id', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=300), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=300), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('educ_attainment', sa.VARCHAR(length=300), autoincrement=False, nullable=False),
    sa.Column('occupation', sa.VARCHAR(length=300), autoincrement=False, nullable=False),
    sa.Column('homeOwner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['homeOwner_id'], ['evacuees.id'], name='dependents_homeOwner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='dependents_pkey'),
    sa.UniqueConstraint('dependents_id', name='dependents_dependents_id_key')
    )
    op.drop_table('household')
    # ### end Alembic commands ###
