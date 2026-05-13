from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_socketio import SocketIO

from config import Config
from services.partido_service import PartidoService
from services.resultado_service import ResultadoService
from services.socket_service import emitir_estado


app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

partido_service = PartidoService()
resultado_service = ResultadoService(Config.RESULTADOS_PATH)


def sincronizar():
    estado = partido_service.obtener_estado()
    emitir_estado(socketio, estado)
    return estado


@app.route("/")
def index():
    return redirect(url_for("control"))


@app.route("/control")
def control():
    return render_template("control.html")


@app.route("/tablero")
def tablero():
    return render_template("tablero.html")


@app.route("/resultados")
def resultados():
    return render_template("resultados.html", resultados=resultado_service.listar())


@app.get("/api/estado")
def api_estado():
    return jsonify(partido_service.obtener_estado())


@app.post("/api/partido/iniciar")
def api_iniciar_partido():
    datos = request.get_json(silent=True) or {}
    try:
        estado = partido_service.iniciar(
            equipo_a=datos.get("equipo_a", ""),
            equipo_b=datos.get("equipo_b", ""),
            modalidad=datos.get("modalidad") or "2_de_3",
        )
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    emitir_estado(socketio, estado)
    return jsonify(estado)


@app.post("/api/puntos/<equipo>/<accion>")
def api_actualizar_puntos(equipo, accion):
    try:
        if accion == "sumar":
            estado = partido_service.sumar_punto(equipo)
        elif accion == "restar":
            estado = partido_service.restar_punto(equipo)
        else:
            return jsonify({"error": "Accion invalida"}), 400
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    emitir_estado(socketio, estado)
    return jsonify(estado)


@app.post("/api/puntos/reiniciar")
def api_reiniciar_puntos():
    estado = partido_service.reiniciar_puntos()
    emitir_estado(socketio, estado)
    return jsonify(estado)


@app.post("/api/partido/finalizar")
def api_finalizar_partido():
    try:
        estado = partido_service.finalizar()
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    resultado_service.guardar(estado)
    emitir_estado(socketio, estado)
    return jsonify(estado)


@socketio.on("connect")
def handle_connect():
    emitir_estado(socketio, partido_service.obtener_estado())


if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
