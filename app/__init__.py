from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from .usuarios.models import Usuario
from .notas.forms import CreateNotaForm  # Importa el formulario

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '3041'  # Cambia esto por una clave secreta real

    login_manager.init_app(app)
    login_manager.login_view = 'usuarios.login'

    from .usuarios.views import usuarios
    app.register_blueprint(usuarios)

    from .notas.views import notas
    app.register_blueprint(notas)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.get_by_id(user_id)
    
    @app.route('/')
    @login_required 
    def index():
        form = CreateNotaForm()  # Crea una instancia del formulario
        return render_template('index.html', form=form)  # Pasa el formulario a la plantilla

    return app