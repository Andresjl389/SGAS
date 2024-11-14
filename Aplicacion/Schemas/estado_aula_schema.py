from pydantic import BaseModel
from uuid import UUID

class EstadoAulaSchema(BaseModel):
    id: UUID
    nombre: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class CreateEstadoAulaSchema(BaseModel):
    nombre: str