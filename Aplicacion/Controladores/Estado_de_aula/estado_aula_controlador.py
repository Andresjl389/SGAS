from typing import Callable
from starlette.requests import Request
from starlette.responses import JSONResponse
from Aplicacion.Schemas.estado_aula_schema import EstadoAulaSchema, CreateEstadoAulaSchema
from Dominio.Entidades.Aulas.estado_aula import Estado_Aula
from Aplicacion.Casos_uso.Estado_de_aula.estado_aula_use_case import EstadoAulaCasoUso
from Dominio.Repositorios.repository import GenericRepository
from sqlalchemy.orm import Session
import json

class EstadoAulaControlador:
    def __init__(self, session: Session):
        self.session = session
        self.repository = GenericRepository(Estado_Aula)
        self.use_case = EstadoAulaCasoUso(self.repository, session)

    async def obtener_estados_aula(self, request: Request) -> JSONResponse:
        try:
            estados = self.use_case.obtener_estados_aula()
            response_data = {
                "data": estados
            }
            return JSONResponse(response_data)
        except Exception as e:
            return JSONResponse({
                "error": "Error al obtener los estados de aula",
                "detail": str(e)
            }, status_code=500)

    async def crear_estado_aula(self, request: Request) -> JSONResponse:
        try:
            data = await request.json()
            create_schema = CreateEstadoAulaSchema(**data)
            nuevo_estado = self.use_case.crear_estado_aula(create_schema)
            
            response_data = {
                "message": "Estado de aula creado exitosamente",
                "data": nuevo_estado
            }
            return JSONResponse(response_data, status_code=201)
        except Exception as e:
            return JSONResponse({
                "error": "Error al crear el estado de aula",
                "detail": str(e)
            }, status_code=500)

    async def actualizar_estado_aula(self, request: Request) -> JSONResponse:
        try:
            estado_aula_id = request.path_params["id"]
            data = await request.json()
            update_schema = CreateEstadoAulaSchema(**data)
            
            estado_actualizado = self.use_case.actualizar_estado_aula(estado_aula_id, update_schema)
            
            response_data = {
                "message": "Estado de aula actualizado exitosamente",
                "data": estado_actualizado
            }
            return JSONResponse(response_data)
        except ValueError as ve:
            return JSONResponse({
                "error": "Error al actualizar el estado de aula",
                "detail": str(ve)
            }, status_code=404)
        except Exception as e:
            return JSONResponse({
                "error": "Error al actualizar el estado de aula",
                "detail": str(e)
            }, status_code=500)

    async def eliminar_estado_aula(self, request: Request) -> JSONResponse:
        try:
            estado_aula_id = request.path_params["id"]
            estado_eliminado = self.use_case.eliminar_estado_aula(estado_aula_id)
            
            response_data = {
                "message": "Estado de aula eliminado exitosamente",
                "data": estado_eliminado
            }
            return JSONResponse(response_data)
        except ValueError as ve:
            return JSONResponse({
                "error": "Error al eliminar el estado de aula",
                "detail": str(ve)
            }, status_code=404)
        except Exception as e:
            return JSONResponse({
                "error": "Error al eliminar el estado de aula",
                "detail": str(e)
            }, status_code=500)