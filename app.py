from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Turnos – Clínica XYZ"

# Ruta fija con tu nombre
@app.route('/usuario')
def usuario():
    return "Bienvenido, Clinton. Tu turno está registrado correctamente."

if __name__ == '__main__':
    app.run(debug=True)
