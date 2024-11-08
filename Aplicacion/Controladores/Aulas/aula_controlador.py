from Aplicacion.Casos_uso.Aulas.aulas_use_case import CrearAulaCasoUso
from Aplicacion.Schemas.aula_schema import AulaSchema
from Infraestructura.Configuracion.configuracion import SessionLocal
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Repositorios.repository import GenericRepository
from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session

class AulaControlador:
    def __init__(self, session: Session):
        repositoy = GenericRepository(Aula)
        self.use_case = CrearAulaCasoUso(repositoy, session)
    
    async def create(self, request: Request):
        data = await request.json()
        aula_data = AulaSchema(**data)
        new_aula = self.use_case.create(aula_data)
        print(aula_data.nombre)
        return JSONResponse(content={"message": "Aula creada", "data": aula_data.nombre}, status_code=201)
    
    async def get(self, request: Request):
        aulas = self.use_case.get_all()
        print("AULAS: ",aulas)
        return JSONResponse(content={"data": aulas}, status_code=200)
