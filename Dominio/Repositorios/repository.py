from typing import TypeVar, Generic, List
from sqlalchemy.orm import Session
from Infraestructura.Configuracion.configuracion import SessionLocal

T = TypeVar('T')

class GenericRepository(Generic[T]):
    def __init__(self, entity_type: T):
        self.entity_type = entity_type

    def __get_session(self):
        return SessionLocal()

    def add(self, entity: T) -> T:
        with self.__get_session() as session:
            session.add(entity)
            session.commit()
            return entity

    def get_all(self) -> List[T]:
        with self.__get_session() as session:
            return session.query(self.entity_type).all()

    def get_by_id(self, id: int) -> T:
        with self.__get_session() as session:
            return session.query(self.entity_type).filter(self.entity_type.id == id).first()

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
