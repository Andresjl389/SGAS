from pydantic import BaseModel
from uuid import UUID

class TipoReservaSchema(BaseModel):
    id: UUID
    nombre: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class CreateTipoReservaSchema(BaseModel):
    nombre: str