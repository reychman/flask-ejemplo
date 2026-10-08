document.addEventListener("DOMContentLoaded", () => {

    const formulario =
        document.querySelector("#form-contacto");

    if (formulario) {
        formulario.addEventListener("submit", (evento) => {
            evento.preventDefault();
            alert("Mensaje enviado correctamente.");
            formulario.reset();
        });
    }

});