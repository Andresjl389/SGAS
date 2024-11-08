from sqlmodel import Session
from Aplicacion.Schemas.aula_schema import AulaSchema
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Repositorios.repository import GenericRepository
from Infraestructura.Configuracion.configuracion import SessionLocal


class CrearAulaCasoUso():
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def create(self, data: AulaSchema) -> Aula:
        print("DATA CASO DE USO", data)
        aula = Aula(**data.dict())
        self.repository.add(aula)
        return aula

    def get_all(self) -> list[Aula]:
        aulas = self.repository.get_all()
        aulas_data = [
            {
                "id": str(aula.id),
                "id_estado_aula": str(aula.id_estado_aula),
                "capacidad": aula.capacidad,
                "nombre": aula.nombre,
                "id_tipo_aula": str(aula.id_tipo_aula)
            }
            for aula in aulas
        ]

        return aulas_data
