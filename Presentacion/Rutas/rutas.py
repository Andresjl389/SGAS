from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route
from Aplicacion.Controladores.Aulas.aula_controlador import AulaControlador
from Aplicacion.Controladores.Tipo_de_aula.tipo_de_aula_controlador import TipoDeAulaControlador

from Infraestructura.Configuracion.configuracion import SessionLocal
from Aplicacion.Controladores.Estado_de_aula.estado_aula_controlador import EstadoAulaControlador

estado_aula_controlador = EstadoAulaControlador(SessionLocal())

tipo_de_aula_controlador = TipoDeAulaControlador(SessionLocal())
aula_controlador = AulaControlador(SessionLocal())

async def home(request):
    return JSONResponse({"message": "Bienvenido a la gestión de asignación de aulas."})

routes =  [
    Route("/", home, methods=["GET"]),
    Route("/aulas", aula_controlador.create, methods=["POST"]),
    Route("/aulas_get", aula_controlador.get, methods=["GET"]),
    Route("/aulas/{id}", aula_controlador.update, methods=["PUT"]),
    Route("/aulas/{id}", aula_controlador.delete, methods=["DELETE"]),
    Route("/tipos_de_aula_crear", tipo_de_aula_controlador.crear_tipo_aula, methods=["POST"]),
    Route("/tipos_de_aula_get", tipo_de_aula_controlador.obtener_tipos_aula, methods=["GET"]),
    Route("/tipos_de_aula/{id}", tipo_de_aula_controlador.eliminar_tipo_aula, methods=["DELETE"]),
    Route("/tipos_de_aula/{id}", tipo_de_aula_controlador.actualizar_tipo_aula, methods=["PUT"]),
    Route("/estados_aula", estado_aula_controlador.obtener_estados_aula, methods=["GET"]),
    Route("/estados_aula/crear", estado_aula_controlador.crear_estado_aula, methods=["POST"]),
    Route("/estados_aula/{id}", estado_aula_controlador.actualizar_estado_aula, methods=["PUT"]),
    Route("/estados_aula/{id}", estado_aula_controlador.eliminar_estado_aula, methods=["DELETE"]),
]

app = Starlette(routes=routes)
