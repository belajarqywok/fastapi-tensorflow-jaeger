"""migrate

Revision ID: 0afd5ba5dcfe
Revises: 75a225bc291a
Create Date: 2023-10-21 15:34:19.237847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0afd5ba5dcfe'
down_revision: Union[str, None] = '75a225bc291a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
