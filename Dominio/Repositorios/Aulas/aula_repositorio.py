

from Dominio.Entidades.Aulas.aula import Aula
from Infraestructura.Configuracion.configuracion import SessionLocal

class AulaRepositorio():
    def __init__(self, ):
        self.db = SessionLocal()

    def obtener_todas(self):
        return self.db.query(Aula).all()
    
    def crear_aula(self, data: Aula):
        self.db.add(data)
        self.db.commit()
        

