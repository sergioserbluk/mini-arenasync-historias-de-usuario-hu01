const form = document.querySelector("#form-iniciar");
const error = document.querySelector("#error");
const estadoTexto = document.querySelector("#estado");
const finalizar = document.querySelector("#finalizar");
const reiniciar = document.querySelector("#reiniciar-puntos");

function setText(id, value) {
    document.querySelector(id).textContent = value;
}

function renderizarControl(estado) {
    setText("#nombre-a", estado.equipo_a || "Equipo A");
    setText("#nombre-b", estado.equipo_b || "Equipo B");
    setText("#puntos-a", estado.puntos.a);
    setText("#puntos-b", estado.puntos.b);
    setText("#sets-a", estado.sets.a);
    setText("#sets-b", estado.sets.b);
    estadoTexto.textContent = estado.ganador
        ? `${estado.mensaje} (${nombreGanador(estado)})`
        : estado.mensaje;
}

async function enviarJson(url, opciones = {}) {
    const respuesta = await fetch(url, {
        method: opciones.method || "POST",
        headers: {"Content-Type": "application/json"},
        body: opciones.body ? JSON.stringify(opciones.body) : undefined,
    });
    const datos = await respuesta.json();
    if (!respuesta.ok) {
        throw new Error(datos.error || "No se pudo completar la accion.");
    }
    return datos;
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    error.textContent = "";
    const datos = new FormData(form);

    try {
        await enviarJson("/api/partido/iniciar", {
            body: {
                equipo_a: datos.get("equipo_a"),
                equipo_b: datos.get("equipo_b"),
                modalidad: datos.get("modalidad") || "2_de_3",
            },
        });
    } catch (err) {
        error.textContent = err.message;
    }
});

document.querySelectorAll("[data-equipo][data-accion]").forEach((boton) => {
    boton.addEventListener("click", async () => {
        error.textContent = "";
        const equipo = boton.dataset.equipo;
        const accion = boton.dataset.accion;
        try {
            await enviarJson(`/api/puntos/${equipo}/${accion}`);
        } catch (err) {
            error.textContent = err.message;
        }




        
    });
});

reiniciar.addEventListener("click", async () => {
    error.textContent = "";
    try {
        await enviarJson("/api/puntos/reiniciar");
    } catch (err) {
        error.textContent = err.message;
    }
});

finalizar.addEventListener("click", async () => {
    error.textContent = "";
    if (!confirm("¿Finalizar y guardar el partido?")) {
        return;
    }
    try {
        await enviarJson("/api/partido/finalizar");
    } catch (err) {
        error.textContent = err.message;
    }
});

cargarEstadoInicial(renderizarControl);
