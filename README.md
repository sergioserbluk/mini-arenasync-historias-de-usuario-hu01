# Mini ArenaSync Voley

Aplicacion web para administrar y mostrar un tablero de voley sincronizado en tiempo real.

## Funciones

- Panel de operador en `/control`.
- Tablero publico en `/tablero`, sin controles.
- Historial de partidos finalizados en `/resultados`.
- Modalidad 2 de 3 o 3 de 5 sets.
- Deteccion automatica de set ganado con 25 puntos y diferencia de 2.
- Correccion de puntos y reversion del ultimo set cerrado.
- Guardado de resultados en `data/resultados.json`, con puntos del ultimo set, puntos totales y diferencia.

## Ejecutar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Luego abrir:

- `http://127.0.0.1:5000/control`
- `http://127.0.0.1:5000/tablero`
- `http://127.0.0.1:5000/resultados`

## Pruebas

```bash
pytest
```
