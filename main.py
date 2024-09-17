import uvicorn
from starlette.responses import JSONResponse
from starlette.routing import Route
from Infraestructura.Configuracion.configuracion import engine, Base
from Presentacion.Rutas.rutas import app

# Crear una ruta para manejar peticiones a la raíz '/'




# Definir las rutas

# Aplicación que usará estas rutas

rutas = app

if __name__ == "__main__":
    # Inicializar la base de datos antes de correr el servidor
    Base.metadata.create_all(bind=engine)
    print("Base de datos inicializada correctamente.")
    
    # Correr el servidor Uvicorn
    uvicorn.run("Presentacion.Rutas.rutas:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
