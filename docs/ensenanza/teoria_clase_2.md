# Teoría Clase 2: API REST con Python y Flask

## Conceptos clave

- API (Interfaz de Programación de Aplicaciones): conjunto de endpoints que permiten comunicar aplicaciones.
- REST: estilo de arquitectura para APIs basado en recursos y métodos HTTP.
- JSON: formato de datos ligero usado para enviar y recibir información entre cliente y servidor.
- Cliente: quien realiza la petición (navegador, `curl`, Postman).
- Servidor: responde las peticiones y procesa la lógica.

## Métodos HTTP importantes

- `GET`: recuperar datos.
- `POST`: enviar datos para crear o actualizar un estado.
- `PUT` / `PATCH`: modificar datos (no usados en este proyecto, pero es bueno conocerlos).
- `DELETE`: eliminar datos (tampoco se usa aquí, pero es parte de REST).

## Flask y rutas

- Decoradores `@app.route` definen las rutas accesibles.
- `request.get_json()` lee el cuerpo JSON de la petición.
- `jsonify()` convierte objetos de Python en JSON.
- Los códigos de respuesta (`200`, `400`, etc.) indican éxito o error.

## Relevancia para el proyecto

En Mini ArenaSync, los endpoints permiten:
- iniciar el partido
- actualizar puntos
- reiniciar el set
- finalizar el partido
- obtener el estado actual

Esto separa la interfaz visual de la lógica del servidor, lo que facilita el mantenimiento y la extensión.
