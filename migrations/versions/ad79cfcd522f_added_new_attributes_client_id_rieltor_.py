"""added new attributes client_id rieltor_id on table messages with names by fk

Revision ID: ad79cfcd522f
Revises: 
Create Date: 2024-08-30 19:58:29.048132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad79cfcd522f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('client_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('rieltor_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_client_msg', 'clients', ['client_id'], ['id'])
        batch_op.create_foreign_key('fk_rieltor_msg', 'rieltors', ['rieltor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_constraint('fk_rieltor_msg', type_='foreignkey')
        batch_op.drop_constraint('fk_client_msg', type_='foreignkey')
        batch_op.drop_column('rieltor_id')
        batch_op.drop_column('client_id')

    # ### end Alembic commands ###
