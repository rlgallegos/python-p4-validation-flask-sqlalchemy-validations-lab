"""Updated

Revision ID: e0dbdd88a7da
Revises: 1fe97901f0d8
Create Date: 2023-04-05 18:37:29.487816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0dbdd88a7da'
down_revision = '1fe97901f0d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.Integer(), nullable=True))
        batch_op.drop_column('phone_numbers')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_numbers', sa.INTEGER(), nullable=True))
        batch_op.drop_column('phone_number')

    # ### end Alembic commands ###
