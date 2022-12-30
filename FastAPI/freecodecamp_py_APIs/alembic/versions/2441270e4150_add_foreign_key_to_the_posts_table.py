"""add foreign-key to the posts table

Revision ID: 2441270e4150
Revises: a19b5b58107e
Create Date: 2022-12-29 13:22:06.530125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2441270e4150'
down_revision = 'a19b5b58107e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", 
                            local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("post_users_fk")
    op.drop_column("posts", "owner_id")
