const arenaSocket = io();

async function cargarEstadoInicial(renderizar) {
    const respuesta = await fetch("/api/estado");
    const estado = await respuesta.json();
    renderizar(estado);
    arenaSocket.on("estado_actualizado", renderizar);
}

function nombreGanador(estado) {
    if (estado.ganador === "a") return estado.equipo_a;
    if (estado.ganador === "b") return estado.equipo_b;
    return "";
}
