from typing import TYPE_CHECKING, List, Optional
from uuid import UUID
from Dominio.Entidades.Base.base_entity import BaseEntity
from sqlmodel import Field, Relationship
from Dominio.Entidades.Usuario.roles import Roles
from Dominio.Entidades.Usuario.estado_usuario import Estado_Usuario



if TYPE_CHECKING:
    from Dominio.Entidades.Reserva.reserva import Reserva
    from Dominio.Entidades.Notificaciones.notificaciones import Notificaciones
    from Dominio.Entidades.Sesion.sesion import Sesion
    from Dominio.Entidades.Registro.solicitud_registro import Solicitud_Registro


class Usuario(BaseEntity, table=True):
    nombre: str = Field(default=None, nullable=False, max_length=50)
    correo: str = Field(default=None, nullable=False, unique=True, max_length=100)
    contraseña: str = Field(default=None, nullable=False)
    id_rol: UUID = Field(default=None, nullable=False, foreign_key="roles.id")
    id_estado_usuario: UUID = Field(default=None, nullable=False, foreign_key="estado_usuario.id")

    roles: Optional[Roles] = Relationship(back_populates="usuario")
    estado_usuario: Optional[Estado_Usuario] = Relationship(back_populates="usuario")
    reservas: List["Reserva"] = Relationship(back_populates="usuario")
    notificaciones: List["Notificaciones"] = Relationship(back_populates="usuario")
    sesion: List["Sesion"] = Relationship(back_populates="usuario")
    solicitud_registro: List["Solicitud_Registro"] = Relationship(back_populates="usuario")