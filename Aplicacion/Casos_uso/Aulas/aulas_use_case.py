from sqlmodel import Session
from Aplicacion.Schemas.aula_schema import AulaSchema, UpdateAulaSchema
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Repositorios.repository import GenericRepository

class CrearAulaCasoUso():
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def create(self, data: AulaSchema) -> Aula:
        aula = Aula(**data.dict())
        return self.repository.add(aula)

    def get_all(self) -> list[dict]:
        return self.repository.get_all_aulas_with_relations()

    def actualizar_aula(self, aula_id: str, data: UpdateAulaSchema) -> dict:
        update_data = data.dict(exclude_unset=True)
        resultado = self.repository.update_aula(aula_id, update_data)
        if not resultado:
            raise ValueError("Aula no encontrada")
        return resultado

    def eliminar_aula(self, aula_id: str) -> dict:
        resultado = self.repository.delete_aula(aula_id)
        if not resultado:
            raise ValueError("Aula no encontrada")
        return resultado