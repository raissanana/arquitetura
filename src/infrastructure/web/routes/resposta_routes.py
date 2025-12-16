from flask import Blueprint, request
from ..container import ContainerFactory

resposta_bp = Blueprint('resposta', __name__)

container = ContainerFactory.get_container()
controller = container.get_resposta_controller()

@resposta_bp.route('/respostas', methods=['POST'])
def criar_resposta():
    return controller.criar_resposta(request)

@resposta_bp.route('/respostas', methods=['GET'])
def listar_respostas():
    return controller.listar_respostas()