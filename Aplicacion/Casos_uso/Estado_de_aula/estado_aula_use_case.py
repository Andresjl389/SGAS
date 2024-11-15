from sqlmodel import Session
from Dominio.Repositorios.repository import GenericRepository
from Dominio.Entidades.Aulas.estado_aula import Estado_Aula
from Aplicacion.Schemas.estado_aula_schema import CreateEstadoAulaSchema

class EstadoAulaCasoUso:
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def obtener_estados_aula(self) -> list[dict]:
        estados = self.repository.get_all()
        estados_data = []
        for estado in estados:
            estado_dict = {
                "id": str(estado.id),
                "nombre": estado.nombre
            }
            estados_data.append(estado_dict)
        return estados_data

    def crear_estado_aula(self, data: CreateEstadoAulaSchema) -> dict:
        estado_aula = Estado_Aula(nombre=data.nombre)
        return self.repository.add(estado_aula)

    def actualizar_estado_aula(self, estado_aula_id: str, data: CreateEstadoAulaSchema) -> dict:
        resultado = self.repository.update(estado_aula_id, {"nombre": data.nombre})
        if not resultado:
            raise ValueError("Estado de aula no encontrado")
        return resultado

    def eliminar_estado_aula(self, estado_aula_id: str) -> dict:
        estado_aula = self.repository.get_by_id(estado_aula_id)
        if not estado_aula:
            raise ValueError("Estado de aula no encontrado")
        
        self.repository.delete(estado_aula)
        return {
            "id": str(estado_aula.id),
            "nombre": estado_aula.nombre
        }