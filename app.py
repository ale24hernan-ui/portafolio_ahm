from flask import Flask, render_template

# Inicializamos la aplicación. Flask buscará automáticamente las carpetas 'templates' y 'static'.
app = Flask(__name__)

# Ruta principal del portafolio
@app.route('/')
def home():
    # Renderizamos la vista del Hero y la estructura base
    return render_template('index.html')

if __name__ == '__main__':
    # Modo debug activado para desarrollo local (recarga automática al guardar)
    app.run(debug=True)