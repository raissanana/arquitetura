# src/application/usecases/listar_formularios.py
from ..dto.formulario_dto import ListarFormulariosOutputDTO
from domain.repositories.formulario_repository import FormularioRepository
from .base_usecase import UseCase

class ListarFormulariosUseCase(UseCase[None, ListarFormulariosOutputDTO]):
    """Use Case para listar formulários"""
    
    def __init__(self, formulario_repository: FormularioRepository):
        self.formulario_repository = formulario_repository
    
    def execute(self, input_dto: None = None) -> ListarFormulariosOutputDTO:
        formularios = self.formulario_repository.listar_formularios()  # ✅ PLURAL
        
        # Converte entidades para dicionários
        formularios_dict = []
        for formulario in formularios:
            formularios_dict.append({
                'id': formulario.id,
                'titulo': formulario.titulo,
                'descricao': formulario.descricao,
                'campos': formulario.campos,
                'criado_em': formulario.criado_em.isoformat()
            })
        
        return ListarFormulariosOutputDTO(formularios=formularios_dict)