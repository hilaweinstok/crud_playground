"""baseline

Revision ID: 4cdb46e1b9d9
Revises: 
Create Date: 2018-06-14 22:01:46.206826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cdb46e1b9d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('catalog',
                    sa.Column('idx', sa.Integer(), nullable=False, index=True, unique=True),
                    sa.Column('product_name', sa.String(length=100), nullable=False),
                    sa.Column('photo_url', sa.String(length=100), nullable=True),
                    sa.Column('barcode', sa.Integer(), nullable=False),
                    sa.Column('price_cents', sa.Integer(), nullable=False),
                    sa.Column('producer', sa.String(length=100), nullable=True),
                    mysql_engine='InnoDB'
                    )
def downgrade():
    op.drop_table('catalog')
