# API

## `GET /api/estado`

Devuelve el estado actual del partido.

## `POST /api/partido/iniciar`

Body:

```json
{
  "equipo_a": "Equipo A",
  "equipo_b": "Equipo B",
  "modalidad": "2_de_3"
}
```

## `POST /api/puntos/<equipo>/sumar`

Suma un punto a `a` o `b`.

## `POST /api/puntos/<equipo>/restar`

Resta un punto a `a` o `b`. Si el ultimo set habia sido otorgado por ese punto, revierte el set.

## `POST /api/puntos/reiniciar`

Reinicia ambos puntos a cero sin modificar sets.

## `POST /api/partido/finalizar`

Finaliza y guarda el resultado. El registro persistido incluye sets, puntos del ultimo set, puntos totales acumulados y diferencia de puntos.
