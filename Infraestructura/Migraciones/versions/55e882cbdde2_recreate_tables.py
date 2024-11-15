"""Recreate tables

Revision ID: 55e882cbdde2
Revises: 10544b7611ca
Create Date: 2024-11-15 13:27:00.003524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy import Column, Integer, String
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '55e882cbdde2'
down_revision: Union[str, None] = '10544b7611ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
     
    if not op.get_bind().has_table('tipo_reserva'):
        op.create_table(
            'tipo_reserva',
            sa.Column('id', sa.String(50), primary_key=True),
            sa.Column('nombre', sa.String(50), nullable=False)
        )
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_reserva',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reserva',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('hora_inicio', sa.DateTime(), nullable=False),
    sa.Column('hora_fin', sa.DateTime(), nullable=False),
    sa.Column('razon_rechazo', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('cantidad_estudiantes', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Uuid(), nullable=False),
    sa.Column('id_aula', sa.Uuid(), nullable=False),
    sa.Column('id_estado_reserva', sa.Uuid(), nullable=False),
    sa.Column('id_tipo_reserva', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['id_aula'], ['aula.id'], ),
    sa.ForeignKeyConstraint(['id_estado_reserva'], ['estado_reserva.id'], ),
    sa.ForeignKeyConstraint(['id_tipo_reserva'], ['tipo_reserva.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserva')
    op.drop_table('tipo_reserva')
    # ### end Alembic commands ###
