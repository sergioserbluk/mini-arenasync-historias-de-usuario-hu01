# Guion de diapositivas y notas del profesor

## Clase 1: Introducción al proyecto y puesta en marcha

### Slide 1: Título
- `Mini ArenaSync`
- “Primera vista: ¿qué hace esta aplicación?”

**Nota:** explicar brevemente la idea general: marcador de voley en tiempo real.

### Slide 2: Objetivo
- Entender estructura del proyecto.
- Ejecutar la app.
- Navegar rutas principales.

**Nota:** reforzar que el curso será práctico.

### Slide 3: Estructura del proyecto
- `app.py`
- `templates/`
- `static/js/`
- `static/css/`
- `services/`
- `data/resultados.json`

**Nota:** mostrar la carpeta en el explorador.

### Slide 4: Rutas principales
- `/control`
- `/tablero`
- `/resultados`

**Nota:** describir qué ve el alumno en cada ruta.

### Slide 5: Instalación y ejecución
- `python -m venv venv`
- `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python app.py`

**Nota:** enfatizar la importancia del entorno virtual.

### Slide 6: Demo en vivo
- Abrir las tres rutas.

**Nota:** si hay problemas de entorno, ayudar a resolverlos.

### Slide 7: Actividad
- Cada alumno levanta la app.
- Explora la interfaz.
- Identifica archivos responsables.

### Slide 8: Tarea
- Documentar funciones de cada ruta.
- Identificar archivos usados.

---

## Clase 2: API REST con Python y Flask

### Slide 1: Título
- `API REST con Flask`

### Slide 2: Objetivo
- Entender endpoints.
- Ver cómo Flask expone APIs.

### Slide 3: ¿Qué es una API?
- Petición HTTP.
- Respuesta JSON.
- Cliente y servidor.

### Slide 4: Endpoints del proyecto
- `GET /api/estado`
- `POST /api/partido/iniciar`
- `POST /api/puntos/<equipo>/<accion>`
- `POST /api/puntos/reiniciar`
- `POST /api/partido/finalizar`

**Nota:** explicar cada uno con ejemplos simples.

### Slide 5: Flujo de datos
- Navegador → `app.py` → servicio → JSON

### Slide 6: Ejemplo práctico
- Llamar `GET /api/estado` con `curl` o Postman.

### Slide 7: Código clave
- `request.get_json()`
- `jsonify()`
- manejo de errores.

### Slide 8: Actividad
- Crear `GET /api/saludo`.
- Probarlo.

### Slide 9: Tarea
- Diagrama request/response.
- Describir endpoints.

---

## Clase 3: Lógica de negocio y persistencia

### Slide 1: Título
- `Lógica de negocio y resultados`

### Slide 2: Objetivo
- Entender la lógica del partido.
- Ver persistencia en JSON.

### Slide 3: Modelo de partido
- `models/partido.py`
- Equipos, puntos, sets, modalidad.

### Slide 4: Servicio de partido
- `services/partido_service.py`
- Funciones principales.

### Slide 5: Reglas de juego
- Set a 25 puntos.
- Diferencia de 2.
- Reiniciar puntos en cada set.

### Slide 6: Persistencia
- `services/resultado_service.py`
- `data/resultados.json`
- Estado en memoria vs archivo.

### Slide 7: Actividad
- Finalizar un partido.
- Analizar el JSON guardado.

### Slide 8: Tarea
- Escribir pseudocódigo de la regla.
- Proponer mejora.

---

## Clase 4: Frontend y sockets en tiempo real

### Slide 1: Título
- `Frontend y sincronización en vivo`

### Slide 2: Objetivo
- Conectar HTML/CSS/JS con SocketIO.
- Ver actualización en vivo.

### Slide 3: Plantillas HTML
- `templates/control.html`
- `templates/tablero.html`
- `templates/resultados.html`

### Slide 4: JavaScript del proyecto
- `static/js/control.js`
- `static/js/socket.js`
- `static/js/tablero.js`

### Slide 5: SocketIO
- Evento `estado_actualizado`.
- Emisión desde backend.

### Slide 6: Flujo en vivo
- Control → backend → evento → tablero.

### Slide 7: Actividad
- Abrir control y tablero en dos pestañas.
- Actualizar puntos.
- Cambiar estilo.

### Slide 8: Tarea
- Escribir el flujo en 5 pasos.
- Proponer mejora visual.

---

## Clase 5: Pruebas y extensiones

### Slide 1: Título
- `Pruebas y mejoras`

### Slide 2: Objetivo
- Validar con tests.
- Proponer mejoras.

### Slide 3: ¿Por qué probar?
- Evitar errores.
- Asegurar comportamiento.

### Slide 4: Tests existentes
- `tests/test_partido.py`
- `tests/test_resultados.py`
- `tests/test_sets.py`

### Slide 5: Ejecutar pruebas
- `pytest`

### Slide 6: Analizar un test
- Entrada / acción / resultado esperado.

### Slide 7: Extensiones posibles
- Historial filtrado.
- Validaciones de formulario.
- Modo oscuro.
- Fecha y hora en resultados.

### Slide 8: Actividad
- Agregar un test.
- Elegir una mejora.

### Slide 9: Tarea
- Proponer nueva función.
- Indicar archivos a modificar.
