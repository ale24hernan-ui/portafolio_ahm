# ¿Por qué?: Importamos la clase Flask y la función render_template desde el paquete flask.
# ¿Para qué?: Flask levanta el servidor backend y render_template procesa los archivos HTML con Jinja2.
from flask import Flask, render_template

# ¿Por qué?: Instanciamos la aplicación pasando __name__ como argumento.
# ¿Para qué?: Para que Flask identifique la raíz del proyecto y localice automáticamente las carpetas 'templates' y 'static'.
app = Flask(__name__)


# =========================================================
# RUTAS DEL ECOSISTEMA INTEGRAL (5 VISTAS)
# =========================================================

# ¿Por qué?: Decorador @app.route('/') vinculado a la raíz del dominio.
# ¿Para qué?: Servir el Hub Generalista donde muestras tu composición 100% integral.
@app.route('/')
def home():
    # ¿Por qué?: Pasamos el parámetro active_page='home' al renderizar index.html.
    # ¿Para qué?: Para que base.html sepa qué enlace del menú debe resaltar visualmente como activo.
    return render_template('index.html', active_page='home')


# ¿Por qué?: Decorador para la ruta '/tecnologia'.
# ¿Para qué?: Aislar en una vista dedicada tus proyectos de software (APEX, Art-Tours) y Ciencia de Datos (TripleTen).
@app.route('/tecnologia')
def tecnologia():
    return render_template('tecnologia.html', active_page='tecnologia')


# ¿Por qué?: Decorador para la ruta '/logistica'.
# ¿Para qué?: Presentar tu autoridad operativa en TSA Comercial, gestión de almacén mayorista B2B y KPIs de Supply Chain.
@app.route('/logistica')
def logistica():
    return render_template('logistica.html', active_page='logistica')


# ¿Por qué?: Decorador para la ruta '/arte'.
# ¿Para qué?: Dedicar una galería exclusiva a tus obras en acrílico y explicar cómo la teoría del color nutre tu diseño UI.
@app.route('/arte')
def arte():
    return render_template('arte.html', active_page='arte')


# ¿Por qué?: Decorador para la ruta '/softskills'.
# ¿Para qué?: Mostrar tu sistema operativo humano: liderazgo de equipos, filosofía (Carnegie, Tracy, Frankl) y certificaciones.
@app.route('/softskills')
def softskills():
    return render_template('softskills.html', active_page='softskills')


# ¿Por qué?: Condicional estándar que verifica si el script se ejecuta directamente.
# ¿Para qué?: Evitar que el servidor de desarrollo se inicie por error si este archivo es importado por Gunicorn en producción (Render).
if __name__ == '__main__':
    # ¿Por qué?: Ejecutamos app.run con debug=True.
    # ¿Para qué?: Activar la recarga automática en local cada vez que guardes cambios en VS Code y ver errores detallados en el navegador.
    app.run(debug=True)