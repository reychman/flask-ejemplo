from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html", titulo="Inicio")


@app.route("/estudiantes")
def estudiantes():
    lista_estudiantes = [
        {"nombre": "Cristopher", "carrera": "Sistemas de Información", "semestre": 5},
        {"nombre": "Ana Torres", "carrera": "Ingeniería de Sistemas", "semestre": 4},
        {"nombre": "Luis Mamani", "carrera": "Ingeniería Informática", "semestre": 6},
    ]
    return render_template(
        "estudiantes.html", titulo="Estudiantes", estudiantes=lista_estudiantes
    )


@app.route("/contacto")
def contacto():
    return render_template("contacto.html", titulo="Contacto")



if __name__ == "__main__":
    app.run(debug=True)
