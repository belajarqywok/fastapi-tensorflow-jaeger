"""migrate

Revision ID: 0ccee8153bed
Revises: 359a5e105f4b
Create Date: 2023-08-24 19:18:23.977118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ccee8153bed'
down_revision: Union[str, None] = '359a5e105f4b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
