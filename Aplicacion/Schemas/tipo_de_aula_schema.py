from pydantic import BaseModel
from uuid import UUID
import json


class CreateTipoDeAulaSchema(BaseModel):
    nombre: str

class UpdateTipoDeAulaSchema(BaseModel):
    nombre: str

class TipoDeAulaSchema(BaseModel):
    id: UUID
    nombre: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        from_attributes = True

    def json(self, **kwargs):
        return json.dumps(self.dict(by_alias=True), default=str, **kwargs)