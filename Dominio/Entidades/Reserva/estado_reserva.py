from typing import TYPE_CHECKING, List
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from Dominio.Entidades.Reserva.reserva import Reserva

class Estado_Reserva(BaseEntity, table=True):
    nombre: str = Field(default=None, nullable=False, max_length=50)

    reserva: List["Reserva"] = Relationship(back_populates="estado_reserva")