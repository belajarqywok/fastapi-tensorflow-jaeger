"""migrate

Revision ID: f06eface0079
Revises: d988fbb037ca
Create Date: 2023-08-24 19:32:22.741346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f06eface0079'
down_revision: Union[str, None] = 'd988fbb037ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
