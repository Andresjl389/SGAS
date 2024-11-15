from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship
from Dominio.Entidades.Base.base_entity import BaseEntity

if TYPE_CHECKING:
    from Dominio.Entidades.Reserva.reserva import Reserva

class Tipo_Reserva(BaseEntity, table=True):
    nombre: str = Field(default=None, nullable=False, max_length=50)

    reserva: List["Reserva"] = Relationship(back_populates="tipo_reserva")
