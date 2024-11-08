from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route
from Aplicacion.Controladores.Aulas.aula_controlador import AulaControlador
from Infraestructura.Configuracion.configuracion import SessionLocal


aula_controlador = AulaControlador(SessionLocal())

async def home(request):
    return JSONResponse({"message": "Bienvenido a la gestión de asignación de aulas."})

routes =  [
    Route("/", home, methods=["GET"]),
    Route("/aulas", aula_controlador.create, methods=["POST"]),
    Route("/aulas_get", aula_controlador.get, methods=["GET"]),
]

app = Starlette(routes=routes)
