# infrastructure/web/container.py
from infrastructure.persistence.neondb.database import Database
from infrastructure.persistence.neondb.formulario_repository import NeonDBFormularioRepository
from infrastructure.persistence.neondb.resposta_repository import NeonDBRespostaRepository
from application.usecases.criar_formulario import CriarFormularioUseCase
from application.usecases.listar_formularios import ListarFormulariosUseCase
from application.usecases.criar_resposta import CriarRespostaUseCase
from application.usecases.listar_respostas import ListarRespostasUseCase
from infrastructure.web.controllers.formulario_controller import FormularioController
from infrastructure.web.controllers.RespostaController import RespostaController  # Você precisa criar

class Container:
    
    def __init__(self):
        # Banco de dados compartilhado
        self.database = Database()
        
        # Repositórios separados
        self.formulario_repository = NeonDBFormularioRepository(self.database)
        self.resposta_repository = NeonDBRespostaRepository(self.database)
    
    def get_formulario_controller(self) -> FormularioController:
        criar_formulario = CriarFormularioUseCase(self.formulario_repository)
        listar_formularios = ListarFormulariosUseCase(self.formulario_repository)
        
        return FormularioController(
            criar_formulario_use_case=criar_formulario,
            listar_formularios_use_case=listar_formularios
        )
    
    def get_resposta_controller(self) -> RespostaController:
        criar_resposta = CriarRespostaUseCase(self.resposta_repository)
        listar_respostas = ListarRespostasUseCase(self.resposta_repository)
        
        return RespostaController(
            criar_resposta_use_case=criar_resposta,
            listar_respostas_use_case=listar_respostas
        )

class ContainerFactory:
    @staticmethod
    def get_container():
        return Container()