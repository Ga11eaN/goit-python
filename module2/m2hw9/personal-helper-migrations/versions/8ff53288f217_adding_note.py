"""Adding note

Revision ID: 8ff53288f217
Revises: 2b307187e2cb
Create Date: 2021-07-04 09:31:35.767149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ff53288f217'
down_revision = '2b307187e2cb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('contacts', sa.Column('note', sa.String(200), nullable=True))


def downgrade():
    op.drop_column('contacts', 'note')
