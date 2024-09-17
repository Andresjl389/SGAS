from pydantic import ValidationError
from starlette.responses import JSONResponse
from Aplicacion.Casos_uso.Aulas.Aulas_consultas import CrearAulaCasoUso
from Aplicacion.Schemas.aula_schema import AulaSchema
from Dominio.Repositorios.Aulas.aula_repositorio import AulaRepositorio


class AulaControlador():
    def __init__(self):
        self.repositorio_aula = AulaRepositorio()
        self.crear_aula_caso = CrearAulaCasoUso(self.repositorio_aula)

    async def crear_aula(self, request):
        try:
            datos = await request.json()
            print("datos: ",datos)
            self.crear_aula_caso.ejecutar(datos)
            return JSONResponse({"mensaje": "Aula creada exitosamente"}, status_code=201)
        except ValidationError as e:
            return JSONResponse({"error": e.errors()}, status_code=400)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)