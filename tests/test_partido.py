import pytest

from services.partido_service import PartidoService


def test_no_inicia_con_nombre_vacio():
    service = PartidoService()

    with pytest.raises(ValueError):
        service.iniciar("Halcones", "")


def test_inicia_con_puntos_y_sets_en_cero():
    service = PartidoService()
    estado = service.iniciar("Halcones", "Tigres")

    assert estado["puntos"] == {"a": 0, "b": 0}
    assert estado["puntos_totales"] == {"a": 0, "b": 0}
    assert estado["sets"] == {"a": 0, "b": 0}
    assert estado["modalidad"] == "2_de_3"
    assert estado["activo"] is True


def test_modo_tres_de_cinco_requiere_tres_sets():
    service = PartidoService()
    service.iniciar("Halcones", "Tigres", "3_de_5")

    for _ in range(2):
        for _ in range(25):
            service.sumar_punto("a")

    estado = service.obtener_estado()
    assert estado["sets"]["a"] == 2
    assert estado["ganador"] is None

    for _ in range(25):
        estado = service.sumar_punto("a")

    assert estado["sets"]["a"] == 3
    assert estado["ganador"] == "a"
