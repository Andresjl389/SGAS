from uuid import UUID
from pydantic import BaseModel, Field
from typing import Optional

class AulaSchema(BaseModel):
    nombre: str
    capacidad: int 
    id_estado_aula: UUID
    id_tipo_aula: UUID

    class Config:
        from_attributes = True
        json_encoders = {UUID: str}
        json_schema_extra = {
            "example":{
                "nombre": "A401",
                "capacidad": 50,
                "id_estado_aula": "95406388-6056-455a-8775-1959b932b",
                "id_tipo_aula": "95406388-6056-455a-8775-1959b932b"
            }
        }

class UpdateAulaSchema(BaseModel):
    nombre: Optional[str] = None
    capacidad: Optional[int] = None
    id_estado_aula: Optional[UUID] = None
    id_tipo_aula: Optional[UUID] = None

    class Config:
        from_attributes = True
        json_encoders = {UUID: str}