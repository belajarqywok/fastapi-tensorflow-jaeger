"""migrate

Revision ID: 75a225bc291a
Revises: cb05e6ed247f
Create Date: 2023-10-21 15:12:11.264878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75a225bc291a'
down_revision: Union[str, None] = 'cb05e6ed247f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
