from typing import Optional
from uuid import UUID
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship
from datetime import date, datetime
from Dominio.Entidades.Usuario.usuario import Usuario

class Notificaciones(BaseEntity, table=True):
    mensaje: str = Field(default=None, nullable=False, max_length=255)
    fecha_envio: datetime = Field(default_factory=datetime.now)
    id_usuario: UUID = Field(default=None, nullable=False, foreign_key="usuario.id")

    usuario: Optional[Usuario] = Relationship(back_populates="notificaciones")