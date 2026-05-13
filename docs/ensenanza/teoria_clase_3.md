# Teoría Clase 3: Lógica de negocio y persistencia

## Conceptos clave

- Modelo de datos: representación estructurada de la información que la aplicación usa.
- Lógica de negocio: reglas que definen cómo funciona la aplicación.
- Persistencia: guardar datos para que sobrevivan después de cerrar la aplicación.
- Estado en memoria: datos que existen sólo mientras el servidor está activo.
- Almacenamiento en archivo: datos guardados en disco, como JSON.

## Por qué separar la lógica

Separar la lógica de negocio del servidor y de la interfaz ayuda a:
- mantener el código ordenado
- reutilizar funciones
- testear la lógica sin depender de la UI

## Reglas de partido en Mini ArenaSync

- El partido puede ser `2_de_3` o `3_de_5` sets.
- Un set se gana con al menos 25 puntos y 2 de diferencia.
- Al cerrar un set, los puntos se reinician pero los sets se conservan.
- Al finalizar el partido se guarda un registro.

## Persistencia en JSON

- `data/resultados.json` almacena los resultados finales.
- JSON es legible y está basado en texto.
- Esta persistencia permite consultar el historial después de apagar el servidor.

## Relevancia para el proyecto

Este nivel de abstracción permite que el servidor pueda procesar reglas complejas sin mezclar la presentación visual con la lógica del juego.
