from ..dto.formulario_dto import ListarFormulariosOutputDTO
from domain.repositories.formulario_repository import FormularioRepository
from .base_usecase import UseCase

class ListarFormulariosUseCase(UseCase[None, ListarFormulariosOutputDTO]):
    """Use Case para listar formulários"""
    
    def __init__(self, formulario_repository: FormularioRepository):
        self.formulario_repository = formulario_repository
    
    def execute(self, input_dto: None = None) -> ListarFormulariosOutputDTO:
        formularios = self.formulario_repository.listar_formularios()
        
        # Converte entidades para dicionários
        formularios_dict = [formulario.to_dict() for formulario in formularios]
        
        return ListarFormulariosOutputDTO(formularios=formularios_dict)