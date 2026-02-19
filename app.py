<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/factura')
def factura():
    return render_template('factura.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask
import os

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Turnos – Clínica XYZ"

# Ruta dinámica de usuario
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"Bienvenido, {nombre}. Tu turno está registrado correctamente."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
>>>>>>> b7f3bd9d68b3855ecd36d23ee87ba76d72b444ba
