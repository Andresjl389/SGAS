from datetime import date, datetime
from typing import Optional
from uuid import UUID
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship
from Dominio.Entidades.Usuario.usuario import Usuario
from Dominio.Entidades.Registro.estado_solicitud_registro import Estado_Solicitud_Registro

class Solicitud_Registro(BaseEntity, table=True):
    fecha_solicitud: datetime = Field(default_factory=datetime.now)
    id_usuario: UUID = Field(default=None, nullable=False, foreign_key="usuario.id")
    id_estado_solicitud_registro: UUID = Field(default=None, nullable=False, foreign_key="estado_solicitud_registro.id")

    usuario: Optional[Usuario] = Relationship(back_populates="solicitud_registro")
    estado_solicitud_registro: Optional[Estado_Solicitud_Registro] = Relationship(back_populates="solicitud_registro")