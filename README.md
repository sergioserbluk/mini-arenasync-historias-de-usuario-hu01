# Mini ArenaSync Voley

Aplicación web para administrar y mostrar un tablero de vóley sincronizado en tiempo real.

## Descarga desde GitHub

1. Abrir una terminal o PowerShell.
2. Clonar el repositorio:

```bash
git clone https://github.com/sergioserbluk/mini-arenasync-historias-de-usuario-hu01.git
```

3. Cambiar al directorio del proyecto:

```bash
cd <repositorio>
```

## Requisitos

- Python 3.8 o superior
- `git` instalado en el equipo

## Configuración local

1. Crear el entorno virtual:

```bash
python -m venv venv
```

2. Activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
python app.py
```

Luego abrir en el navegador:

- `http://127.0.0.1:5000/control`
- `http://127.0.0.1:5000/tablero`
- `http://127.0.0.1:5000/resultados`

## Pruebas

Para ejecutar los tests del proyecto:

```bash
pytest
```

## Funciones principales

- Panel de operador en `/control`
- Tablero público en `/tablero`, sin controles
- Historial de partidos finalizados en `/resultados`
- Modalidad 2 de 3 o 3 de 5 sets
- Detección automática de set ganado con 25 puntos y diferencia de 2
- Corrección de puntos y reversión del último set cerrado
- Guardado de resultados en `data/resultados.json`, con puntos del último set, puntos totales y diferencia
