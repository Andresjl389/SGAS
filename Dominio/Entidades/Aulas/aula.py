from typing import Optional
from uuid import UUID
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship
from Dominio.Entidades.Aulas.estado_aula import Estado_Aula
from Dominio.Entidades.Aulas.tipo_aula import Tipo_Aula

class Aula(BaseEntity, table=True):
    nombre: str = Field(default=None, nullable=False, max_length=50)
    capacidad: int = Field(default=None, nullable=False)
    id_estado_aula: UUID = Field(default=None, nullable=False, foreign_key="estado_aula.id")
    id_tipo_aula: UUID = Field(default=None, nullable=False, foreign_key="tipo_aula.id")

    estado_aula: Optional[Estado_Aula] = Relationship(back_populates="aula")
    tipo_aula: Optional[Tipo_Aula] = Relationship(back_populates="aula")