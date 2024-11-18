from typing import List, TypeVar, Generic, Dict
from sqlalchemy.orm import Session
from Infraestructura.Configuracion.configuracion import SessionLocal
from Dominio.Entidades.Aulas.aula import Aula
from Dominio.Entidades.Aulas.estado_aula import Estado_Aula
from Dominio.Entidades.Aulas.tipo_aula import Tipo_Aula

T = TypeVar('T')

class GenericRepository(Generic[T]):
    def __init__(self, entity_type: T):
        self.entity_type = entity_type

    def __get_session(self):
        return SessionLocal()
    
    def add(self, entity: T) -> dict:
        with self.__get_session() as session:
            session.add(entity)
            session.commit()
            result = {
                "id": str(entity.id),
                "nombre": entity.nombre
            }
            print(f"Repository result: {result}")  # Para debugging
            return result
        
    def update(self, entity_id: str, data: dict) -> T:
        with self.__get_session() as session:
            entity = session.query(self.entity_type).filter_by(id=entity_id).first()
            if entity:
                for key, value in data.items():
                    setattr(entity, key, value)
                session.commit()
                return {
                    "id": str(entity.id),
                    "nombre": entity.nombre
                }
            return None

    def get_all(self) -> List[dict]:
        with self.__get_session() as session:
            entities = session.query(self.entity_type).all()
            return [{"id": str(entity.id), "nombre": entity.nombre} for entity in entities]

    def get_by_id(self, entity_id: str) -> T:
        with self.__get_session() as session:
            return session.query(self.entity_type).filter_by(id=entity_id).first()

    def delete(self, entity: T):
        with self.__get_session() as session:
            session.delete(entity)
            session.commit()

    def read_by_options(self, *criterion) -> List[T]:
        with self.__get_session() as session:
            query = session.query(self.entity_type)
            for crit in criterion:
                query = query.filter(crit)
            return query.all()

    def delete_by_options(self, *criterion):
        with self.__get_session() as session:
            query = session.query(self.entity_type)
            for crit in criterion:
                query = query.filter(crit)
            instances = query.all()
            for instance in instances:
                session.delete(instance)
            session.commit()    
    def get_all_aulas_with_relations(self) -> List[Dict]:
        with self.__get_session() as session:
            aulas = session.query(Aula)\
                .join(Estado_Aula)\
                .join(Tipo_Aula)\
                .all()
            
            return [self._format_aula_data(aula, session) for aula in aulas]

    def _format_aula_data(self, aula: Aula, session: Session) -> Dict:
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

    def update_aula(self, aula_id: str, data: dict) -> Dict:
        with self.__get_session() as session:
            aula = session.query(Aula).filter_by(id=aula_id).first()
            if not aula:
                return None
            
            for key, value in data.items():
                if value is not None:
                    setattr(aula, key, value)
            
            session.commit()
            return self._format_aula_data(aula, session)

    def delete_aula(self, aula_id: str) -> Dict:
        with self.__get_session() as session:
            aula = session.query(Aula).filter_by(id=aula_id).first()
            if not aula:
                return None
            
            aula_data = self._format_aula_data(aula, session)
            session.delete(aula)
            session.commit()
            return aula_data
