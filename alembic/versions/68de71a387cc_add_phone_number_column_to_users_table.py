"""add phone_number column to users table

Revision ID: 68de71a387cc
Revises: 
Create Date: 2026-08-02 21:33:35.370115

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68de71a387cc'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
    "users",
    sa.Column("phone_number", sa.String(20), nullable=True)
)


def downgrade() -> None:
    """Downgrade schema."""
    pass
