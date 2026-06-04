"""create tasks table

Revision ID: 03cb2f28b140
Revises: 
Create Date: 2026-06-04 22:26:56.082874

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = '03cb2f28b140'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
