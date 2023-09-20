"""migrate

Revision ID: cb05e6ed247f
Revises: 0a24327f2e57
Create Date: 2023-08-26 16:16:30.773469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb05e6ed247f'
down_revision: Union[str, None] = '0a24327f2e57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
