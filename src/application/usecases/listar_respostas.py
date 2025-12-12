# src/application/usecases/listar_respostas.py
from ..dto.formulario_dto import ListarRespostasOutputDTO
from domain.repositories.formulario_repository import FormularioRepository
from .base_usecase import UseCase

class ListarRespostasUseCase(UseCase[None, ListarRespostasOutputDTO]):
    """Use Case para listar respostas"""
    
    def __init__(self, formulario_repository: FormularioRepository):
        self.formulario_repository = formulario_repository
    
    def execute(self, input_dto: None = None) -> ListarRespostasOutputDTO:
        respostas = self.formulario_repository.listar_respostas()
        
        # Converte entidades para dicionários
        respostas_dict = [resposta.to_dict() for resposta in respostas]
        
        return ListarRespostasOutputDTO(respostas=respostas_dict)