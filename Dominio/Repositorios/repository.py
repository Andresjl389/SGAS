
from typing import List, TypeVar, Generic
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
            # Crear y retornar un diccionario con los datos antes de cerrar la sesión
            return {
                "id": str(entity.id),
                "nombre": entity.nombre
            }

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

    def get_all(self) -> List[T]:
        with self.__get_session() as session:
            if self.entity_type == Aula:
                return session.query(self.entity_type)\
                    .join(Estado_Aula)\
                    .join(Tipo_Aula)\
                    .all()
            return session.query(self.entity_type).all()

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
