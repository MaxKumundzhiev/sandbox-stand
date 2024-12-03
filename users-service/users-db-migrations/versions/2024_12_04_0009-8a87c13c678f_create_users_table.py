"""create users table

Revision ID: 8a87c13c678f
Revises: 
Create Date: 2024-12-04 00:09:22.413920

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8a87c13c678f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("nickname", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("nickname"),
    )


def downgrade() -> None:
    op.drop_table("users")
