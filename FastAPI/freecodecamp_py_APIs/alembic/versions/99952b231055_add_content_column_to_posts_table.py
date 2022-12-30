"""add content column to posts table

Revision ID: 99952b231055
Revises: 177eb129c95c
Create Date: 2022-12-29 12:42:38.657188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99952b231055'
down_revision = '177eb129c95c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column("posts", "content")
