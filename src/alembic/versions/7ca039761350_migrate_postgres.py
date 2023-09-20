"""migrate postgres

Revision ID: 7ca039761350
Revises: c615cb1cbb7d
Create Date: 2023-08-23 14:30:08.342560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ca039761350'
down_revision: Union[str, None] = 'c615cb1cbb7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
