"""add user table

Revision ID: a19b5b58107e
Revises: 99952b231055
Create Date: 2022-12-29 12:49:25.635521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a19b5b58107e'
down_revision = '99952b231055'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", 
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )


def downgrade() -> None:
    op.drop_table("users")
