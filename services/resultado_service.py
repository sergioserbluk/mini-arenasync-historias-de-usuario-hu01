import json
from pathlib import Path


class ResultadoService:
    def __init__(self, ruta):
        self.ruta = Path(ruta)
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        if not self.ruta.exists():
            self.ruta.write_text("[]", encoding="utf-8")

    def listar(self):
        try:
            return json.loads(self.ruta.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def guardar(self, resultado):
        resultados = self.listar()
        resultados.append(
            {
                "equipo_a": resultado["equipo_a"],
                "equipo_b": resultado["equipo_b"],
                "sets_a": resultado["sets"]["a"],
                "sets_b": resultado["sets"]["b"],
                "puntos_a": resultado["puntos"]["a"],
                "puntos_b": resultado["puntos"]["b"],
                "puntos_totales_a": resultado["puntos_totales"]["a"],
                "puntos_totales_b": resultado["puntos_totales"]["b"],
                "diferencia_puntos": resultado["puntos_totales"]["a"] - resultado["puntos_totales"]["b"],
                "modalidad": resultado["modalidad_label"],
                "fecha_hora": resultado["fecha_hora"],
                "ganador": resultado.get("ganador"),
            }
        )
        self.ruta.write_text(json.dumps(resultados, indent=2, ensure_ascii=False), encoding="utf-8")
        return resultados[-1]
