"""migrate

Revision ID: 2150a1fde263
Revises: f06eface0079
Create Date: 2023-08-24 19:41:34.303173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2150a1fde263'
down_revision: Union[str, None] = 'f06eface0079'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
