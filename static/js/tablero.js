function setText(id, value) {
    document.querySelector(id).textContent = value;
}

function renderizarTablero(estado) {
    setText("#nombre-a", estado.equipo_a || "Equipo A");
    setText("#nombre-b", estado.equipo_b || "Equipo B");
    setText("#puntos-a", estado.puntos.a);
    setText("#puntos-b", estado.puntos.b);
    setText("#sets-a", estado.sets.a);
    setText("#sets-b", estado.sets.b);
    setText("#modalidad", estado.modalidad_label);
    setText("#estado", estado.ganador ? `${estado.mensaje}: ${nombreGanador(estado)}` : estado.mensaje);
}

cargarEstadoInicial(renderizarTablero);
