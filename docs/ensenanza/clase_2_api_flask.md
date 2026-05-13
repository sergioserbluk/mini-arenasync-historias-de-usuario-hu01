# Clase 2: API REST con Python y Flask

## Objetivo

- Comprender qué es un endpoint.
- Ver cómo Flask expone rutas API.
- Conectar el backend con las peticiones del frontend.

## Contenido

1. ¿Qué es una API REST?
   - Peticiones HTTP.
   - Respuestas en JSON.
   - Cliente y servidor.

2. Endpoints del proyecto
   - `GET /api/estado`
   - `POST /api/partido/iniciar`
   - `POST /api/puntos/<equipo>/<accion>`
   - `POST /api/puntos/reiniciar`
   - `POST /api/partido/finalizar`

3. Código clave
   - Revisar `app.py`.
   - Explicar `request.get_json()` y `jsonify()`.
   - Manejo de errores con `400`.

4. Ejemplo práctico
   - Usar `curl` o Postman para probar `GET /api/estado`.
   - Ver la respuesta JSON.

## Actividad en clase

- Crear un endpoint adicional en `app.py`:
  - `GET /api/saludo`
  - Respuesta: `{"mensaje": "Hola desde Mini ArenaSync"}`
- Probarlo con `curl` o navegador.

## Tarea

- Dibujar el flujo request/response en un diagrama simple.
- Describir qué hace cada endpoint y qué datos recibe/envía.
