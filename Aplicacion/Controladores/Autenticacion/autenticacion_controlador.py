from urllib.request import Request
from sqlmodel import Session
from Aplicacion.Casos_uso.Autenticacion.autenticacion_use_case import AutenticacionCasoUso
from Aplicacion.Schemas.usuario_schema import UsuarioSchema
from Dominio.Entidades.Usuario.usuario import Usuario
from Dominio.Repositorios.repository import GenericRepository
from starlette.responses import JSONResponse

class AutenticacionControlador:
    def __init__(self, session: Session):
        self.session = session
        self.repository = GenericRepository(Usuario)
        self.use_case = AutenticacionCasoUso(session, self.repository)


    async def register(self, request: Request):
        try:
            data = await request.json()
            create_schema = UsuarioSchema(**data)
            nuevo_usuario = self.use_case.register_user(create_schema)
            response_data = {
                "message": "Usuario creado exitosamente",
                "data": nuevo_usuario
            }
            return JSONResponse(response_data, status_code=201)
        except Exception as e:
            return JSONResponse({
                "error": "error al crear al usuario",
                "details": str(e),
            }, status_code=500)