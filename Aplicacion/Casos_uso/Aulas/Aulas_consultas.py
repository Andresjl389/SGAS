from Aplicacion.Schemas.aula_schema import AulaSchema
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Repositorios.Aulas.aula_repositorio import AulaRepositorio


class CrearAulaCasoUso():
    def __init__(self, aula_repositorio: AulaRepositorio):
        self.aula_repositorio = aula_repositorio
    
    def ejecutar(self, data: AulaSchema):
        nueva_aula = Aula(
            nombre=data["nombre"],
            capacidad=data["capacidad"],
            id_tipo_aula=data["id_tipo_aula"],
            id_estado_aula=data["id_estado_aula"]
        )
        return self.aula_repositorio.crear_aula(nueva_aula)