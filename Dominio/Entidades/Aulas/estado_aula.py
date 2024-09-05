from typing import TYPE_CHECKING, List
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from Dominio.Entidades.Aulas.aula import Aula

class Estado_Aula(BaseEntity, table=True):
    nombre: str = Field(default=None, nullable=False, max_length=50)

    aulas: List["Aula"] = Relationship(back_populates="estado_aula")

