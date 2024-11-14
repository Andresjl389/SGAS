from sqlmodel import Session
from Aplicacion.Schemas.aula_schema import AulaSchema
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Entidades.Aulas.estado_aula import Estado_Aula
from Dominio.Entidades.Aulas.tipo_aula import Tipo_Aula
from Dominio.Repositorios.repository import GenericRepository
from Infraestructura.Configuracion.configuracion import SessionLocal
from Aplicacion.Schemas.aula_schema import UpdateAulaSchema

class CrearAulaCasoUso():
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def create(self, data: AulaSchema) -> Aula:
        aula = Aula(**data.dict())
        self.repository.add(aula)
        return aula

    def get_all(self) -> list[dict]:
        with SessionLocal() as session:
            aulas = session.query(Aula)\
                .join(Estado_Aula)\
                .join(Tipo_Aula)\
                .all()
                
            aulas_data = []
            for aula in aulas:
                aula_dict = {
                    "id": str(aula.id),
                    "nombre": aula.nombre,
                    "capacidad": aula.capacidad,
                    "estado_aula": {
                        "id": str(aula.id_estado_aula),
                        "nombre": session.get(Estado_Aula, aula.id_estado_aula).nombre
                    },
                    "tipo_aula": {
                        "id": str(aula.id_tipo_aula),
                        "nombre": session.get(Tipo_Aula, aula.id_tipo_aula).nombre
                    }
                }
                aulas_data.append(aula_dict)
            
            return aulas_data

    def actualizar_aula(self, aula_id: str, data: UpdateAulaSchema) -> dict:
        with SessionLocal() as session:
            aula = session.query(Aula).filter_by(id=aula_id).first()
            if not aula:
                raise ValueError("Aula no encontrada")
            
            # Actualizar solo los campos que vienen en data
            update_data = data.dict(exclude_unset=True)
            for key, value in update_data.items():
                if value is not None:  # Solo actualizar si el valor no es None
                    setattr(aula, key, value)
            
            session.commit()
            
            return {
                "id": str(aula.id),
                "nombre": aula.nombre,
                "capacidad": aula.capacidad,
                "estado_aula": {
                    "id": str(aula.id_estado_aula),
                    "nombre": session.get(Estado_Aula, aula.id_estado_aula).nombre
                },
                "tipo_aula": {
                    "id": str(aula.id_tipo_aula),
                    "nombre": session.get(Tipo_Aula, aula.id_tipo_aula).nombre
                }
            }

    def eliminar_aula(self, aula_id: str) -> dict:
        with SessionLocal() as session:
            aula = session.query(Aula).filter_by(id=aula_id).first()
            if not aula:
                raise ValueError("Aula no encontrada")
            
            # Guardar datos antes de eliminar
            aula_data = {
                "id": str(aula.id),
                "nombre": aula.nombre,
                "capacidad": aula.capacidad,
                "estado_aula": {
                    "id": str(aula.id_estado_aula),
                    "nombre": session.get(Estado_Aula, aula.id_estado_aula).nombre
                },
                "tipo_aula": {
                    "id": str(aula.id_tipo_aula),
                    "nombre": session.get(Tipo_Aula, aula.id_tipo_aula).nombre
                }
            }
            
            session.delete(aula)
            session.commit()
            
            return aula_data