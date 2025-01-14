"""sss

Revision ID: 407d35e790ca
Revises: 978ea2e4bb95
Create Date: 2025-01-14 17:50:11.795791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '407d35e790ca'
down_revision = '978ea2e4bb95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name desription', sa.String(length=250), nullable=True))
        batch_op.drop_column('description')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)

    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.VARCHAR(length=250), nullable=True))
        batch_op.drop_column('name desription')

    # ### end Alembic commands ###
