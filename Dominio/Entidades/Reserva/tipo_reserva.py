from typing import List
from Dominio.Entidades.Base.base_entity import BaseEntity  
from sqlmodel import Field, Relationship
from Dominio.Entidades.Base.base_entity import BaseEntity

class Tipo_Reserva(BaseEntity, table=True):
    __tablename__ = "tipo_reserva"
    nombre: str = Field(default=None, nullable=False, max_length=50)

    @property
    def reservas(self) -> List["Reserva"]:
        return Relationship(back_populates="tipo_reserva")