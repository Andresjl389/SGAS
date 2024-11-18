from uuid import UUID
from pydantic import BaseModel, Field


class UsuarioSchema(BaseModel):
    __tablename__ = "usuarios"
    nombre: str = Field(default=None, nullable=False, max_length=50)
    correo: str = Field(default=None, nullable=False, unique=True, max_length=100)
    contraseña: str = Field(default=None, nullable=False)
    id_rol: UUID = Field(default=None, nullable=False, foreign_key="roles.id")
    id_estado_usuario: UUID = Field(default=None, nullable=False, foreign_key="estado_usuario.id")

    class Config:
        json_schema_extra = {
            "example":{
                "usuario": {
                    "nombre": "John Doe",
                    "correo": "john.doe@example.com",
                    "contraseña": "password123",
                    "id_rol": "6b48ad78-87f5-45ff-8d03-89c99676beb1",
                    "id_estado_usuario": "be5dedd5-e6bb-4569-8258-72fa61f26dd1"
                }
            }
        }