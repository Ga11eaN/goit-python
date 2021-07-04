"""Adding name, mail, phone, address

Revision ID: 2b307187e2cb
Revises: 
Create Date: 2021-07-04 09:11:38.415356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b307187e2cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contacts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(40), nullable=False),
        sa.Column('phone', sa.String(12), nullable=True),
        sa.Column('address', sa.String(40), nullable=True),
        sa.Column('mail', sa.String(20), nullable=True),
        sa.Column('birthday', sa.String(10), nullable=True),
    )


def downgrade():
    op.drop_table('contacts')
