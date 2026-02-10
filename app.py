from flask import Flask
import os

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Turnos – Clínica XYZ"

# Ruta fija con tu nombre
@app.route('/usuario')
def usuario():
    return "Bienvenido, Clinton. Tu turno está registrado correctamente."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
