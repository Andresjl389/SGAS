from typing import TYPE_CHECKING, List
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from Dominio.Entidades.Registro.solicitud_registro import Solicitud_Registro

class Estado_Solicitud_Registro(BaseEntity, table=True):
    nombre: str = Field(default=None, nullable=False, max_length=50)

    solicitud_registro: List["Solicitud_Registro"] = Relationship(back_populates="estado_solicitud_registro")