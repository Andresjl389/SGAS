from sqlmodel import Session
from Dominio.Entidades.Usuario.usuario import Usuario
from Dominio.Repositorios.repository import GenericRepository
from Infraestructura.Autenticacion.jwt_helper import JWTManager
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AutenticacionCasoUso:
    def __init__(self, session: Session, repository: GenericRepository):
        self.session = session
        self.repository = repository


    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    def register_user(self, data: Usuario):
        hased_password = self.hash_password(data.contraseña)
        usuario = Usuario(
            nombre=data.nombre,
            correo=data.correo,
            contraseña=hased_password,
            id_rol=data.id_rol,
            id_estado_usuario=data.id_estado_usuario
        )
        return self.repository.add(usuario)