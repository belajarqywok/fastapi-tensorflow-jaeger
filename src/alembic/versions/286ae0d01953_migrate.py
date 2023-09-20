"""migrate

Revision ID: 286ae0d01953
Revises: 0ccee8153bed
Create Date: 2023-08-24 19:21:08.262651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '286ae0d01953'
down_revision: Union[str, None] = '0ccee8153bed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
