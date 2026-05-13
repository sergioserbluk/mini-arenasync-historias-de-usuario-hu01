from copy import deepcopy
from datetime import datetime

from models.partido import MODALIDADES, Partido


class PartidoService:
    def __init__(self):
        self.partido = Partido()

    def obtener_estado(self):
        return self.partido.to_dict()

    def iniciar(self, equipo_a, equipo_b, modalidad="2_de_3"):
        equipo_a = equipo_a.strip()
        equipo_b = equipo_b.strip()

        if not equipo_a or not equipo_b:
            raise ValueError("Debe cargar el nombre de ambos equipos.")

        if modalidad not in MODALIDADES:
            modalidad = "2_de_3"

        self.partido = Partido(
            equipo_a=equipo_a,
            equipo_b=equipo_b,
            modalidad=modalidad,
            activo=True,
            finalizado=False,
            mensaje="Partido activo",
            fecha_inicio=datetime.now().isoformat(timespec="seconds"),
        )
        return self.obtener_estado()

    def sumar_punto(self, equipo):
        self._validar_equipo_y_partido(equipo)
        if self.partido.ganador:
            raise ValueError("El partido ya tiene un ganador.")

        self.partido.puntos[equipo] += 1
        self.partido.puntos_totales[equipo] += 1
        self.partido.ultimo_set = None
        self._verificar_set(equipo)
        return self.obtener_estado()

    def restar_punto(self, equipo):
        self._validar_equipo_y_partido(equipo)

        if self.partido.ultimo_set and self.partido.ultimo_set["ganador"] == equipo:
            self._revertir_ultimo_set()
            return self.obtener_estado()

        if self.partido.puntos[equipo] > 0:
            self.partido.puntos[equipo] -= 1
            self.partido.puntos_totales[equipo] = max(0, self.partido.puntos_totales[equipo] - 1)

        self.partido.mensaje = "Partido activo"
        return self.obtener_estado()

    def reiniciar_puntos(self):
        if not self.partido.activo:
            raise ValueError("No hay un partido activo.")

        for equipo, puntos in self.partido.puntos.items():
            self.partido.puntos_totales[equipo] = max(0, self.partido.puntos_totales[equipo] - puntos)
        self.partido.puntos = {"a": 0, "b": 0}
        self.partido.ultimo_set = None
        self.partido.mensaje = "Puntos reiniciados"
        return self.obtener_estado()

    def finalizar(self):
        if not self.partido.activo:
            raise ValueError("No hay un partido activo para finalizar.")

        self.partido.activo = False
        self.partido.finalizado = True
        self.partido.fecha_fin = datetime.now().isoformat(timespec="seconds")
        if not self.partido.ganador:
            if self.partido.sets["a"] > self.partido.sets["b"]:
                self.partido.ganador = "a"
            elif self.partido.sets["b"] > self.partido.sets["a"]:
                self.partido.ganador = "b"
        self.partido.mensaje = "Partido finalizado y guardado"
        return self.partido.preparar_resultado()

    def _validar_equipo_y_partido(self, equipo):
        if equipo not in {"a", "b"}:
            raise ValueError("Equipo invalido.")
        if not self.partido.activo:
            raise ValueError("No hay un partido activo.")

    def _verificar_set(self, equipo):
        rival = "b" if equipo == "a" else "a"
        puntos_equipo = self.partido.puntos[equipo]
        puntos_rival = self.partido.puntos[rival]

        if puntos_equipo >= 25 and puntos_equipo - puntos_rival >= 2:
            estado_previo = {
                "puntos": deepcopy(self.partido.puntos),
                "puntos_totales": deepcopy(self.partido.puntos_totales),
                "sets": deepcopy(self.partido.sets),
                "ganador_partido": self.partido.ganador,
                "mensaje": self.partido.mensaje,
            }

            self.partido.sets[equipo] += 1
            self.partido.puntos = {"a": 0, "b": 0}
            self.partido.ultimo_set = {
                "ganador": equipo,
                "estado_previo": estado_previo,
            }
            self.partido.mensaje = f"Set para {self.partido.equipo_nombre(equipo)}"
            self._verificar_partido(equipo)

    def _verificar_partido(self, equipo):
        if self.partido.sets[equipo] >= self.partido.sets_para_ganar:
            self.partido.ganador = equipo
            self.partido.mensaje = f"Ganador del partido: {self.partido.equipo_nombre(equipo)}"

    def _revertir_ultimo_set(self):
        estado_previo = self.partido.ultimo_set["estado_previo"]
        self.partido.puntos = deepcopy(estado_previo["puntos"])
        self.partido.puntos_totales = deepcopy(estado_previo["puntos_totales"])
        self.partido.sets = deepcopy(estado_previo["sets"])
        self.partido.ganador = estado_previo["ganador_partido"]
        self.partido.mensaje = "Set revertido por correccion"
        equipo = self.partido.ultimo_set["ganador"]
        if self.partido.puntos[equipo] > 0:
            self.partido.puntos[equipo] -= 1
            self.partido.puntos_totales[equipo] = max(0, self.partido.puntos_totales[equipo] - 1)
        self.partido.ultimo_set = None
