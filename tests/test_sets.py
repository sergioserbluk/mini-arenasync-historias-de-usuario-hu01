from services.partido_service import PartidoService


def test_otorga_set_con_25_y_diferencia_de_dos():
    service = PartidoService()
    service.iniciar("Halcones", "Tigres")

    for _ in range(24):
        service.sumar_punto("a")
        service.sumar_punto("b")

    estado = service.sumar_punto("a")
    assert estado["sets"]["a"] == 0
    assert estado["puntos"] == {"a": 25, "b": 24}
    assert estado["puntos_totales"] == {"a": 25, "b": 24}

    estado = service.sumar_punto("a")
    assert estado["sets"]["a"] == 1
    assert estado["puntos"] == {"a": 0, "b": 0}
    assert estado["puntos_totales"] == {"a": 26, "b": 24}


def test_resta_no_deja_puntos_negativos():
    service = PartidoService()
    service.iniciar("Halcones", "Tigres")

    estado = service.restar_punto("a")

    assert estado["puntos"]["a"] == 0
    assert estado["puntos_totales"]["a"] == 0


def test_resta_revierte_ultimo_set():
    service = PartidoService()
    service.iniciar("Halcones", "Tigres")

    for _ in range(25):
        estado = service.sumar_punto("a")

    assert estado["sets"]["a"] == 1
    assert estado["puntos"] == {"a": 0, "b": 0}
    assert estado["puntos_totales"] == {"a": 25, "b": 0}

    estado = service.restar_punto("a")

    assert estado["sets"]["a"] == 0
    assert estado["puntos"] == {"a": 24, "b": 0}
    assert estado["puntos_totales"] == {"a": 24, "b": 0}


def test_reiniciar_puntos_descuenta_puntos_del_set_actual():
    service = PartidoService()
    service.iniciar("Halcones", "Tigres")

    service.sumar_punto("a")
    service.sumar_punto("a")
    service.sumar_punto("b")
    estado = service.reiniciar_puntos()

    assert estado["puntos"] == {"a": 0, "b": 0}
    assert estado["puntos_totales"] == {"a": 0, "b": 0}


def test_resultado_incluye_puntos_totales():
    service = PartidoService()
    service.iniciar("Halcones", "Tigres")

    for _ in range(25):
        service.sumar_punto("a")
    service.sumar_punto("b")

    resultado = service.finalizar()

    assert resultado["puntos"] == {"a": 0, "b": 1}
    assert resultado["puntos_totales"] == {"a": 25, "b": 1}
