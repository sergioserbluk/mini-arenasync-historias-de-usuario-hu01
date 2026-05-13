from services.resultado_service import ResultadoService


def test_guardar_resultado_persiste_puntos_totales_y_diferencia(tmp_path):
    service = ResultadoService(tmp_path / "resultados.json")

    registro = service.guardar(
        {
            "equipo_a": "Halcones",
            "equipo_b": "Tigres",
            "sets": {"a": 2, "b": 1},
            "puntos": {"a": 0, "b": 18},
            "puntos_totales": {"a": 75, "b": 64},
            "modalidad_label": "2 de 3 sets",
            "fecha_hora": "2026-05-08T11:00:00",
            "ganador": "a",
        }
    )

    assert registro["puntos_totales_a"] == 75
    assert registro["puntos_totales_b"] == 64
    assert registro["diferencia_puntos"] == 11
