from typing import TYPE_CHECKING, List
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from Dominio.Entidades.Usuario.usuario import Usuario

class Roles(BaseEntity, table=True):
    nombre: str = Field(default=None, nullable=False, max_length=50)

    usuario: List["Usuario"] = Relationship(back_populates="roles")