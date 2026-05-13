from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime


MODALIDADES = {
    "2_de_3": {"label": "2 de 3 sets", "sets_para_ganar": 2},
    "3_de_5": {"label": "3 de 5 sets", "sets_para_ganar": 3},
}


@dataclass
class Partido:
    equipo_a: str = ""
    equipo_b: str = ""
    modalidad: str = "2_de_3"
    puntos: dict = field(default_factory=lambda: {"a": 0, "b": 0})
    puntos_totales: dict = field(default_factory=lambda: {"a": 0, "b": 0})
    sets: dict = field(default_factory=lambda: {"a": 0, "b": 0})
    activo: bool = False
    finalizado: bool = False
    ganador: str | None = None
    mensaje: str = "Sin partido activo"
    fecha_inicio: str | None = None
    fecha_fin: str | None = None
    ultimo_set: dict | None = None

    @property
    def sets_para_ganar(self):
        return MODALIDADES[self.modalidad]["sets_para_ganar"]

    @property
    def modalidad_label(self):
        return MODALIDADES[self.modalidad]["label"]

    def equipo_nombre(self, equipo):
        return self.equipo_a if equipo == "a" else self.equipo_b

    def to_dict(self):
        return {
            "equipo_a": self.equipo_a,
            "equipo_b": self.equipo_b,
            "modalidad": self.modalidad,
            "modalidad_label": self.modalidad_label,
            "puntos": deepcopy(self.puntos),
            "puntos_totales": deepcopy(self.puntos_totales),
            "sets": deepcopy(self.sets),
            "activo": self.activo,
            "finalizado": self.finalizado,
            "ganador": self.ganador,
            "mensaje": self.mensaje,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
        }

    def preparar_resultado(self):
        datos = self.to_dict()
        datos["fecha_hora"] = self.fecha_fin or datetime.now().isoformat(timespec="seconds")
        return datos
