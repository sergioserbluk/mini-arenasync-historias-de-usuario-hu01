# Hoja de ruta didáctica: Mini ArenaSync

## Objetivo general

Utilizar Mini ArenaSync como proyecto práctico para enseñar:

- API REST en Python con Flask
- Sockets en tiempo real con Flask-SocketIO
- Frontend con HTML, CSS y JavaScript
- Separación de lógica de negocio y persistencia
- Pruebas con `pytest`

## Estructura del curso

### Clase 1 - Introducción y puesta en marcha
- Revisar la estructura del proyecto.
- Ejecutar la aplicación localmente.
- Navegar las rutas principales.
- Revisar `teoria_clase_1.md`.
- Actividad: levantar la app y explorar la interfaz.

### Clase 2 - API REST con Python y Flask
- Entender qué es un endpoint.
- Revisar los endpoints definidos en `app.py`.
- Probar llamadas HTTP con `curl` o un cliente.
- Revisar `teoria_clase_2.md`.
- Actividad: crear un endpoint nuevo.

### Clase 3 - Lógica de negocio y persistencia
- Analizar `models/partido.py` y `services/partido_service.py`.
- Revisar el guardado de resultados en JSON.
- Revisar `teoria_clase_3.md`.
- Actividad: interpretar y proponer mejoras en las reglas del partido.

### Clase 4 - Frontend y sockets en tiempo real
- Revisar plantillas HTML y JavaScript.
- Explicar la sincronización entre `control` y `tablero`.
- Revisar `teoria_clase_4.md`.
- Actividad: modificar estilos y observar la sincronización en vivo.

### Clase 5 - Pruebas y extensiones
- Revisar los tests existentes.
- Ejecutar `pytest`.
- Revisar `teoria_clase_5.md`.
- Proponer mejoras y agregar un test nuevo.

## Material adicional

- Las presentaciones de cada clase están en los archivos `clase_*.md`.
- El guion para el profesor está en `diapositivas_guion.md`.
