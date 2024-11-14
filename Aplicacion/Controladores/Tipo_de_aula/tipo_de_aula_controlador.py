from typing import Callable
from starlette.requests import Request
from starlette.responses import JSONResponse
from Aplicacion.Schemas.tipo_de_aula_schema import TipoDeAulaSchema, CreateTipoDeAulaSchema, UpdateTipoDeAulaSchema
from Dominio.Entidades.Aulas.tipo_aula import Tipo_Aula
from Aplicacion.Casos_uso.Tipo_de_aula.tipo_de_aula_use_case import ObtenerTiposDeAulaCasoUso, CrearTipoDeAulaCasoUso, EliminarTipoDeAulaCasoUso, ActualizarTipoDeAulaCasoUso
from Dominio.Repositorios.repository import GenericRepository
from sqlalchemy.orm import Session
import json

class TipoDeAulaControlador:
    def __init__(self, session: Session):
        self.session = session
        self.repository = GenericRepository(Tipo_Aula)
        self.use_case = ObtenerTiposDeAulaCasoUso(self.repository, session)
        self.create_use_case = CrearTipoDeAulaCasoUso(self.repository, session)
        self.delete_use_case = EliminarTipoDeAulaCasoUso(self.repository, session)
        self.update_use_case = ActualizarTipoDeAulaCasoUso(self.repository, session)

    async def eliminar_tipo_aula(self, request: Request) -> JSONResponse:
        try:
            tipo_aula_id = request.path_params["id"]  # Obtiene el ID de los parámetros de la URL
            tipo_aula = self.delete_use_case.eliminar_tipo_aula(tipo_aula_id)
            
            response_data = {
                "message": "Tipo de aula eliminado exitosamente",
                "data": tipo_aula
            }
            return JSONResponse(response_data)
        except ValueError as ve:
            return JSONResponse({
                "error": "Error al eliminar el tipo de aula",
                "detail": str(ve)
            }, status_code=404)
        except Exception as e:
            return JSONResponse({
                "error": "Error al eliminar el tipo de aula",
                "detail": str(e)
            }, status_code=500)
        
    async def obtener_tipos_aula(self, request: Request) -> JSONResponse:
        try:
            tipos_aula = self.use_case.obtener_tipos_aula()
            tipos_aula_schema = [TipoDeAulaSchema.from_orm(tipo) for tipo in tipos_aula]
            response_data = {
                "data": [json.loads(tipo.json()) for tipo in tipos_aula_schema]
            }
            return JSONResponse(response_data)
        except Exception as e:
            return JSONResponse({"error": "Error al obtener los tipos de aula.", "detail": str(e)}, status_code=500)

    async def crear_tipo_aula(self, request: Request) -> JSONResponse:
        try:
            data = await request.json()
            create_schema = CreateTipoDeAulaSchema(**data)
            resultado = self.create_use_case.crear_tipo_aula(create_schema)
            
            response_data = {
                "message": "Tipo de aula creado exitosamente",
                "data": resultado
            }
            return JSONResponse(response_data, status_code=201)
        except Exception as e:
            return JSONResponse({
                "error": "Error al crear el tipo de aula.",
                "detail": str(e)
            }, status_code=500)
    async def actualizar_tipo_aula(self, request: Request) -> JSONResponse:
        try:
            tipo_aula_id = request.path_params["id"]
            data = await request.json()
            update_schema = UpdateTipoDeAulaSchema(**data)
            
            tipo_aula_actualizado = self.update_use_case.actualizar_tipo_aula(tipo_aula_id, update_schema)
            
            response_data = {
                "message": "Tipo de aula actualizado exitosamente",
                "data": tipo_aula_actualizado
            }
            return JSONResponse(response_data)
        except ValueError as ve:
            return JSONResponse({
                "error": "Error al actualizar el tipo de aula",
                "detail": str(ve)
            }, status_code=404)
        except Exception as e:
            return JSONResponse({
                "error": "Error al actualizar el tipo de aula",
                "detail": str(e)
            }, status_code=500)

