import uvicorn
from Infraestructura.Configuracion.configuracion import engine, SessionLocal, Base

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    body = f'Received {scope["method"]} request to {scope["path"]}'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': body.encode('utf-8'),
    })

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Base de datos inicializada correctamente.")

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
