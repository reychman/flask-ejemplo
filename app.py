from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html", titulo="Inicio")


@app.route("/estudiantes")
def estudiantes():
    estudiantes = [
        {
            "nombre": "Ana López",
            "carrera": "Ingeniería de Sistemas",
            "semestre": 4
        },
        {
            "nombre": "Carlos Pérez",
            "carrera": "Informática",
            "semestre": 3
        },
        {
            "nombre": "María García",
            "carrera": "Ingeniería de Sistemas",
            "semestre": 5
        }
    ]

    return render_template(
        "estudiantes.html",
        titulo="Estudiantes",
        estudiantes=estudiantes
    )


@app.route("/contacto")
def contacto():
    return render_template(
        "contacto.html",
        titulo="Contacto"
    )


if __name__ == "__main__":
    app.run(debug=True)