from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Registrar rotas
    from . import routes
    app.register_blueprint(routes.bp)

    return app