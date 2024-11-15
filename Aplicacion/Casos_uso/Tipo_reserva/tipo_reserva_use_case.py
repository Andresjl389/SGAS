from sqlmodel import Session
from Dominio.Repositorios.repository import GenericRepository
from Dominio.Entidades.Reserva.tipo_reserva import Tipo_Reserva
from Aplicacion.Schemas.tipo_reserva_schema import CreateTipoReservaSchema

class TipoReservaCasoUso:
    def __init__(self, repository: GenericRepository, session: Session):
        self.repository = repository
        self.session = session

    def obtener_tipos_reserva(self) -> list[dict]:
        tipos = self.repository.get_all()
        return tipos

    def crear_tipo_reserva(self, data: CreateTipoReservaSchema) -> dict:
        tipo_reserva = Tipo_Reserva(nombre=data.nombre)
        try:
            resultado = self.repository.add(tipo_reserva)
            return {
                "id": str(tipo_reserva.id),
                "nombre": tipo_reserva.nombre
            }
        except Exception as e:
            print(f"Error en caso de uso: {str(e)}")  # Para debugging
            raise

    def actualizar_tipo_reserva(self, tipo_reserva_id: str, data: CreateTipoReservaSchema) -> dict:
        resultado = self.repository.update(tipo_reserva_id, {"nombre": data.nombre})
        if not resultado:
            raise ValueError("Tipo de reserva no encontrado")
        return resultado

    def eliminar_tipo_reserva(self, tipo_reserva_id: str) -> dict:
        tipo_reserva = self.repository.get_by_id(tipo_reserva_id)
        if not tipo_reserva:
            raise ValueError("Tipo de reserva no encontrado")
        self.repository.delete(tipo_reserva)
        return {"id": str(tipo_reserva.id), "nombre": tipo_reserva.nombre}