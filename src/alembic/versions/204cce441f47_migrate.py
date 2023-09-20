"""migrate

Revision ID: 204cce441f47
Revises: 286ae0d01953
Create Date: 2023-08-24 19:29:02.096523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '204cce441f47'
down_revision: Union[str, None] = '286ae0d01953'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
