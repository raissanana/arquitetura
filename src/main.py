from flask import Flask
from infrastructure.web.routes.formulario_routes import formulario_bp  # ✅ formulario_bp, não formulario_routes
from infrastructure.web.routes.resposta_routes import resposta_bp      # ✅ resposta_bp, não resposta_routes

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['JSON_SORT_KEYS'] = False
    
    # Registrar blueprints
    app.register_blueprint(formulario_bp, url_prefix='/api')  # ✅ formulario_bp
    app.register_blueprint(resposta_bp, url_prefix='/api')    # ✅ resposta_bp
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)