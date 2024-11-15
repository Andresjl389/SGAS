from sqlmodel import Session
from Dominio.Repositorios.repository import GenericRepository
from Dominio.Entidades.Aulas.tipo_aula import Tipo_Aula
from Aplicacion.Schemas.tipo_de_aula_schema import CreateTipoDeAulaSchema, UpdateTipoDeAulaSchema,TipoDeAulaSchema

class CrearTipoDeAulaCasoUso:
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def crear_tipo_aula(self, data: CreateTipoDeAulaSchema) -> dict:
        tipo_aula = Tipo_Aula(nombre=data.nombre)
        return self.repository.add(tipo_aula)

class ObtenerTiposDeAulaCasoUso:
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def obtener_tipos_aula(self):
        return self.repository.get_all()  # Debe devolver una lista de instancias de `Tipo_Aula`

class EliminarTipoDeAulaCasoUso:
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def eliminar_tipo_aula(self, tipo_aula_id: str) -> dict:
        tipo_aula = self.repository.get_by_id(tipo_aula_id)
        if not tipo_aula:
            raise ValueError("Tipo de aula no encontrado")
            
        self.repository.delete(tipo_aula)
        return {
            "id": str(tipo_aula.id),
            "nombre": tipo_aula.nombre
        }

class ActualizarTipoDeAulaCasoUso:
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def actualizar_tipo_aula(self, tipo_aula_id: str, data: UpdateTipoDeAulaSchema) -> dict:
        resultado = self.repository.update(tipo_aula_id, {"nombre": data.nombre})
        if not resultado:
            raise ValueError("Tipo de aula no encontrado")
        return resultado