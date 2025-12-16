# src/application/usecases/listar_respostas.py
from ..dto.resposta_dto import ListarRespostasOutputDTO
from domain.repositories.resposta_repository import RespostaRepository
from .base_usecase import UseCase

class ListarRespostasUseCase(UseCase[None, ListarRespostasOutputDTO]):
    """Use Case para listar respostas"""
    
    def __init__(self, resposta_repository: RespostaRepository):
        self.resposta_repository = resposta_repository
    
    def execute(self, input_dto: None = None) -> ListarRespostasOutputDTO:
        respostas = self.resposta_repository.listar_respostas()  # ✅ PLURAL
        
        # Converte entidades para dicionários
        respostas_dict = []
        for resposta in respostas:
            respostas_dict.append({
                'id': resposta.id,
                'formulario_id': resposta.formulario_id,
                'agente_nome': resposta.agente_nome,
                'dados': resposta.dados,
                'criado_em': resposta.criado_em.isoformat()
            })
        
        return ListarRespostasOutputDTO(respostas=respostas_dict)