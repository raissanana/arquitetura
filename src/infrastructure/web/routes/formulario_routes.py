from flask import Blueprint, request
from ..container import ContainerFactory

formulario_bp = Blueprint('formulario', __name__)

container = ContainerFactory.get_container()
controller = container.get_formulario_controller()

@formulario_bp.route('/formularios', methods=['POST'])
def criar_formulario():
    return controller.criar_formulario(request)

@formulario_bp.route('/formularios', methods=['GET'])
def listar_formularios():
    return controller.listar_formularios()

@formulario_bp.route('/respostas', methods=['POST'])
def criar_resposta():
    return controller.criar_resposta(request)

@formulario_bp.route('/respostas', methods=['GET'])
def listar_respostas():
    return controller.listar_respostas()

formulario_routes = formulario_bp