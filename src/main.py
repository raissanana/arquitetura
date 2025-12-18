from flask import Flask
from infrastructure.web.routes.formulario_routes import formulario_bp 
from infrastructure.web.routes.resposta_routes import resposta_bp    

def create_app():
    app = Flask(__name__)
    
    app.config['JSON_SORT_KEYS'] = False
    
    app.register_blueprint(formulario_bp, url_prefix='/api')
    app.register_blueprint(resposta_bp, url_prefix='/api') 
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)