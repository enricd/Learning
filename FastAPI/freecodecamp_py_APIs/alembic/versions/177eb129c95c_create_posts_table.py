"""create posts table

Revision ID: 177eb129c95c
Revises: 
Create Date: 2022-12-29 12:26:49.201978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '177eb129c95c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", 
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("posts")
