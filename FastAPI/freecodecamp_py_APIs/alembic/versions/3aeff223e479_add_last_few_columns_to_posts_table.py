"""add last few columns to posts table

Revision ID: 3aeff223e479
Revises: 2441270e4150
Create Date: 2022-12-29 14:01:21.788789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aeff223e479'
down_revision = '2441270e4150'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
