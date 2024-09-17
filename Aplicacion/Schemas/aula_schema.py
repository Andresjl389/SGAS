from uuid import UUID
from pydantic import BaseModel, Field


class AulaSchema(BaseModel):
    nombre: str
    capacidad: int 
    id_estado_aula: UUID
    id_tipo_aula: UUID

    class Config:
        json_schema_extra = {
            "example":{
                "nombre": "A401",
                "capacidad": 50,
                "id_estado_aula": "95406388-6056-455a-8775-1959b932b",
                "id_tipo_aula": "95406388-6056-455a-8775-1959b932b"
            }
        }