# Arquitectura

La aplicacion usa Flask para rutas HTTP y Flask-SocketIO para sincronizar el tablero en tiempo real.

- `app.py`: rutas, endpoints y eventos SocketIO.
- `models/partido.py`: estructura del estado del partido.
- `services/partido_service.py`: reglas de negocio.
- `services/resultado_service.py`: persistencia en JSON.
- `templates/`: pantallas HTML.
- `static/js/`: comportamiento del panel y tablero.
- `static/css/`: estilos visuales.

El estado activo vive en memoria. Los partidos finalizados se guardan en `data/resultados.json`.

El marcador visible del set se almacena en `puntos`; el acumulado real del encuentro se almacena en `puntos_totales`. Esto permite reiniciar los puntos al cerrar un set sin perder la sumatoria final del partido.
