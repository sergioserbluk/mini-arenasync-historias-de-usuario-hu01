# Teoría Clase 4: Frontend y sockets en tiempo real

## Conceptos clave

- Frontend: parte de la aplicación que se ejecuta en el navegador.
- HTML: estructura de la página web.
- CSS: estilos visuales.
- JavaScript: comportamiento e interacciones en el cliente.
- WebSocket / SocketIO: canal de comunicación bidireccional en tiempo real.

## Por qué usar sockets

- Las APIs REST son excelentes para solicitudes puntuales.
- En tiempo real, se necesitan actualizaciones instantáneas sin recargar la página.
- SocketIO facilita este tipo de conexión persistente y eficiente.

## Flujo de sincronización

1. El navegador se conecta al servidor mediante SocketIO.
2. El servidor emite eventos cuando cambia el estado del partido.
3. El cliente recibe esos eventos y actualiza la vista.
4. Esto permite sincronizar `/control` y `/tablero` en tiempo real.

## Relevancia para el proyecto

En Mini ArenaSync, el tablero debe reflejar inmediatamente los cambios hechos por el operador. El uso de SocketIO hace posible que todos los usuarios vean el mismo estado sin refrescar manualmente.
