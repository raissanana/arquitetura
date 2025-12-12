from flask import Flask
from infrastructure.web.routes.formulario_routes import formulario_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(formulario_routes, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)