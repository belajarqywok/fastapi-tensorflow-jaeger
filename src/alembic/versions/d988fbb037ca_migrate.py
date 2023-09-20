"""migrate

Revision ID: d988fbb037ca
Revises: da7ce2db6fa5
Create Date: 2023-08-24 19:30:42.602515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd988fbb037ca'
down_revision: Union[str, None] = 'da7ce2db6fa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
