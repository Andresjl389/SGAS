import jwt
from datetime import datetime, timedelta
from typing import Dict
from Infraestructura.Configuracion.configuracion import settings

class JWTManager:
    @staticmethod
    def generate_token(data: Dict) -> str:
        expiration = datetime.utcnow() + timedelta(seconds=settings.EXPIRATION)
        payload = {
            "exp": expiration,
            "iat": datetime.utcnow(),
            "data": data
        }

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
            )
    
    @staticmethod
    def verify_token(token: str) -> Dict:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            return payload["data"]
        except jwt.ExpiredSignatureError:
            raise ValueError("El tokenha expirado")
        except jwt.InvalidTokenError:
            raise ValueError("Token inválido")