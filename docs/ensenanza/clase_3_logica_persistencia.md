# Clase 3: Lógica de negocio y persistencia

## Objetivo

- Entender la representación del estado del partido.
- Revisar las reglas de negocio en `services/partido_service.py`.
- Ver cómo se guarda el historial en JSON.

## Contenido

1. Modelo de partido
   - `models/partido.py`
   - Equipos, puntos, sets y modalidad.

2. Servicio de partido
   - `services/partido_service.py`
   - `iniciar()`
   - `sumar_punto()`
   - `restar_punto()`
   - `reiniciar_puntos()`
   - `finalizar()`

3. Reglas de juego
   - Set se cierra a 25 puntos.
   - La diferencia debe ser al menos 2 puntos.
   - Al finalizar un set, se reinician los puntos.

4. Persistencia
   - `services/resultado_service.py`
   - `data/resultados.json`
   - Estado en memoria vs almacenamiento en archivo.

## Actividad en clase

- Finalizar un partido en la app.
- Abrir `data/resultados.json` y revisar el resultado guardado.
- Identificar qué datos se almacenan.

## Tarea

- Escribir pseudocódigo para la regla de ganar un set.
- Proponer una mejora simple, por ejemplo agregar la fecha del partido.
