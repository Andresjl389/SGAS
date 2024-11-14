from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session
from Dominio.Repositorios.repository import GenericRepository
from Dominio.Entidades.Reserva.tipo_reserva import Tipo_Reserva
from Aplicacion.Casos_uso.Tipo_reserva.tipo_reserva_use_case import TipoReservaCasoUso
from Aplicacion.Schemas.tipo_reserva_schema import CreateTipoReservaSchema

class TipoReservaControlador:
    def __init__(self, session: Session):
        self.repository = GenericRepository(Tipo_Reserva)
        self.use_case = TipoReservaCasoUso(self.repository, session)

    async def obtener_tipos_reserva(self, request: Request):
        try:
            tipos = self.use_case.obtener_tipos_reserva()
            return JSONResponse({"data": tipos})
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    async def crear_tipo_reserva(self, request: Request):
        try:
            data = await request.json()
            tipo_data = CreateTipoReservaSchema(**data)
            nuevo_tipo = self.use_case.crear_tipo_reserva(tipo_data)
            return JSONResponse({
                "message": "Tipo de reserva creado exitosamente",
                "data": nuevo_tipo
            }, status_code=201)
        except Exception as e:
            return JSONResponse({
                "error": "Error al crear el tipo de reserva",
                "detail": str(e)
            }, status_code=500)

    async def actualizar_tipo_reserva(self, request: Request):
        try:
            tipo_id = request.path_params["id"]
            data = await request.json()
            tipo_data = CreateTipoReservaSchema(**data)
            tipo_actualizado = self.use_case.actualizar_tipo_reserva(tipo_id, tipo_data)
            return JSONResponse({
                "message": "Tipo de reserva actualizado exitosamente",
                "data": tipo_actualizado
            })
        except ValueError as ve:
            return JSONResponse({"error": str(ve)}, status_code=404)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    async def eliminar_tipo_reserva(self, request: Request):
        try:
            tipo_id = request.path_params["id"]
            tipo_eliminado = self.use_case.eliminar_tipo_reserva(tipo_id)
            return JSONResponse({
                "message": "Tipo de reserva eliminado exitosamente",
                "data": tipo_eliminado
            })
        except ValueError as ve:
            return JSONResponse({"error": str(ve)}, status_code=404)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)