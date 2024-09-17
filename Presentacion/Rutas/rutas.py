from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.routing import Route
from Aplicacion.Controladores.Aulas.aula_controlador import AulaControlador


aula_controlador = AulaControlador()

async def home(request):
    return JSONResponse({"message": "Bienvenido a la gestión de asignación de aulas."})

routes =  [
    Route("/", home, methods=["GET"]),
    # Route("/aulas", obtener_asignacion, methods=["GET"]),
    Route("/aulas", aula_controlador.crear_aula, methods=["POST"]),  # Agregar la ruta para crear aulas
]

app = Starlette(routes=routes)

# # Crear una ruta para manejar otra funcionalidad (por ejemplo, crear asignaciones)
# async def crear_asignacion(request):
#     # Aquí recibirías datos de asignación desde el cuerpo de la solicitud POST
#     datos_asignacion = await request.json()  # Obtener datos del body en JSON
#     return JSONResponse({"status": "success", "data": datos_asignacion})

# async def obtener_asignacion():
#     return AulaControlador.obtener_aulas()