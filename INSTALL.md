# Instalación

## Clonar desde GitHub

```bash
git https://github.com/sergioserbluk/mini-arenasync-historias-de-usuario-hu01.git
cd <repositorio>
```

## Preparar el entorno

1. Crear el entorno virtual:

```bash
python -m venv venv
```

2. Activarlo en Windows:

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

## Abrir en el navegador

- `http://127.0.0.1:5000/control`
- `http://127.0.0.1:5000/tablero`
- `http://127.0.0.1:5000/resultados`

## Probar el proyecto

```bash
pytest
```

> Si es la primera vez que usas el proyecto, asegúrate de tener Python 3.8+ instalado y `git` disponible en tu equipo.
