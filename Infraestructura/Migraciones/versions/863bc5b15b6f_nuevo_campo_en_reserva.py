"""Nuevo campo en Reserva

Revision ID: 863bc5b15b6f
Revises: 848b4791c3ea
Create Date: 2024-11-13 20:17:46.483319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '863bc5b15b6f'
down_revision: Union[str, None] = '848b4791c3ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reserva', sa.Column('cantidad_estudiantes', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reserva', 'cantidad_estudiantes')
    # ### end Alembic commands ###