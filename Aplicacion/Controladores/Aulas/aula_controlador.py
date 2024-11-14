from Aplicacion.Casos_uso.Aulas.aulas_use_case import CrearAulaCasoUso
from Aplicacion.Schemas.aula_schema import AulaSchema, UpdateAulaSchema
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Repositorios.repository import GenericRepository
from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session

class AulaControlador:
    def __init__(self, session: Session):
        self.repository = GenericRepository(Aula)
        self.use_case = CrearAulaCasoUso(self.repository, session)
    
    async def create(self, request: Request):
        try:
            data = await request.json()
            aula_data = AulaSchema(**data)
            new_aula = self.use_case.create(aula_data)
            return JSONResponse({
                "message": "Aula creada exitosamente",
                "data": new_aula
            }, status_code=201)
        except Exception as e:
            return JSONResponse({
                "error": "Error al crear el aula",
                "detail": str(e)
            }, status_code=500)

    async def get(self, request: Request):
        try:
            aulas = self.use_case.get_all()
            return JSONResponse({"data": aulas}, status_code=200)
        except Exception as e:
            return JSONResponse({
                "error": "Error al obtener las aulas",
                "detail": str(e)
            }, status_code=500)

    async def update(self, request: Request):
        try:
            aula_id = request.path_params["id"]
            data = await request.json()
            aula_data = UpdateAulaSchema(**data)
            aula_actualizada = self.use_case.actualizar_aula(aula_id, aula_data)
            return JSONResponse({
                "message": "Aula actualizada exitosamente",
                "data": aula_actualizada
            })
        except ValueError as ve:
            return JSONResponse({"error": "Error al actualizar el aula", "detail": str(ve)}, status_code=404)
        except Exception as e:
            return JSONResponse({"error": "Error al actualizar el aula", "detail": str(e)}, status_code=500)

    async def delete(self, request: Request):
        try:
            aula_id = request.path_params["id"]
            aula_eliminada = self.use_case.eliminar_aula(aula_id)
            return JSONResponse({
                "message": "Aula eliminada exitosamente",
                "data": aula_eliminada
            })
        except ValueError as ve:
            return JSONResponse({"error": "Error al eliminar el aula", "detail": str(ve)}, status_code=404)
        except Exception as e:
            return JSONResponse({"error": "Error al eliminar el aula", "detail": str(e)}, status_code=500)