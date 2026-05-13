# Clase 4: Frontend y sockets en tiempo real

## Objetivo

- Comprender cómo interactúan HTML, CSS y JavaScript.
- Ver cómo SocketIO sincroniza el tablero en vivo.
- Conectar la lógica del operador con el tablero público.

## Contenido

1. HTML y plantillas
   - `templates/control.html`
   - `templates/tablero.html`
   - `templates/resultados.html`

2. JavaScript
   - `static/js/control.js`
   - `static/js/socket.js`
   - `static/js/tablero.js`

3. SocketIO
   - Evento `estado_actualizado`.
   - Emisión desde `services/socket_service.py`.
   - Conexión desde el frontend.

4. Flujo en vivo
   - Botón de control → backend → evento SocketIO → tablero se actualiza.

## Actividad en clase

- Abrir `/control` y `/tablero` en dos ventanas.
- Actualizar puntos y observar la sincronización.
- Cambiar una etiqueta o color en el CSS.

## Tarea

- Escribir el flujo de interacción en 5 pasos.
- Proponer una mejora visual para la interfaz del tablero.
