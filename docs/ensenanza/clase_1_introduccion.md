# Clase 1: Introducción al proyecto y puesta en marcha

## Objetivo

- Entender la estructura del proyecto Mini ArenaSync.
- Ejecutar la aplicación localmente.
- Navegar las rutas principales del servidor.

## Contenido

1. ¿Qué hace la aplicación?
   - Panel de operador: `/control`
   - Tablero público: `/tablero`
   - Historial de partidos: `/resultados`

2. Estructura del proyecto
   - `app.py` — servidor Flask y API.
   - `templates/` — vistas HTML.
   - `static/js/` — lógica del frontend.
   - `static/css/` — estilos.
   - `services/` — lógica del partido y persistencia.
   - `data/resultados.json` — historial guardado.

3. Instalación y ejecución
   - `python -m venv venv`
   - `venv\Scripts\activate`
   - `pip install -r requirements.txt`
   - `python app.py`

4. Demo en vivo
   - Abrir `http://127.0.0.1:5000/control`
   - Abrir `http://127.0.0.1:5000/tablero`
   - Abrir `http://127.0.0.1:5000/resultados`

## Actividad en clase

- Cada alumno levanta la app en su máquina.
- Explora la interfaz de control y el tablero.
- Identifica en el código qué archivos generan cada ruta.

## Tarea

- Documentar en pocas frases qué hace cada ruta HTTP.
- Anotar qué archivos se usan para cada pantalla de la aplicación.
