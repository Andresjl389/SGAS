from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID
from sqlmodel import Field, DateTime, func, Relationship
from Dominio.Entidades.Base.base_entity import BaseEntity
from Dominio.Entidades.Usuario.usuario import Usuario

class Sesion(BaseEntity, table=True):
    inicio_sesion: datetime = Field(sa_type=DateTime(timezone=True), default=func.now())
    fin_sesion: datetime = Field(sa_type=DateTime(timezone=True), default_factory=lambda: datetime.now() + timedelta(minutes=30))
    id_usuario: UUID = Field(default=None, nullable=False, foreign_key="usuario.id")

    usuario: Optional[Usuario] = Relationship(back_populates="sesion")