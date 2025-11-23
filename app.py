from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", titulo="Template Flask")

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre}! Esta respuesta viene desde Flask."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
