"""migrate

Revision ID: da7ce2db6fa5
Revises: 204cce441f47
Create Date: 2023-08-24 19:30:03.446946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da7ce2db6fa5'
down_revision: Union[str, None] = '204cce441f47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
