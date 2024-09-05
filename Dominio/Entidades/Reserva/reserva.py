from typing import Optional
from uuid import UUID
from Dominio.Entidades.Base.base_entity import BaseEntity
from datetime import date, datetime, time, timedelta
from sqlmodel import Field, DateTime, func, Relationship
from Dominio.Entidades.Usuario.usuario import Usuario
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Entidades.Reserva.estado_reserva import Estado_Reserva


class Reserva(BaseEntity, table=True):
    fecha: datetime = Field(default_factory=date.today, nullable=False)
    hora_inicio: datetime = Field(nullable=False)
    hora_fin: datetime = Field(nullable=False)
    razon_rechazo: Optional[str] = Field(default=None, max_length=255)
    id_usuario: UUID = Field(default=None, nullable=False, foreign_key="usuario.id")
    id_aula: UUID = Field(default=None, nullable=False, foreign_key="aula.id")
    id_estado_reserva: UUID = Field(default=None, nullable=False, foreign_key="estado_reserva.id")

    usuario: Optional[Usuario] = Relationship(back_populates="reserva")
    aula: Optional[Aula] = Relationship(back_populates="reserva")
    estado_reserva: Optional[Estado_Reserva] = Relationship(back_populates="reserva")